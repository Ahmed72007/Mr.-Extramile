# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime
import wikipedia
from ddgs import DDGS
from ollama import chat  # Ollama Python client

app = FastAPI(title="AI Research API")

# ----------------- Enable CORS -----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:3001"],
        # Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- Data Models -----------------
class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: List[str]

# ----------------- Helper Functions -----------------
def save_to_txt(text: str, filename="research_output.txt"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"--- {ts} ---\n{text}\n\n")

def wiki_lookup(query: str) -> str:
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation, options: {e.options[:5]}"
    except:
        return ""

def ddg_lookup(query: str) -> str:
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, safesearch="Off", timelimit="y"):
                results.append(r["body"])
                if len(results) >= 3:
                    break
        return "\n".join(results)
    except:
        return ""

# ----------------- API Endpoint -----------------
@app.post("/query", response_model=ResearchResponse)
def query_ai(request: ResearchRequest):
    sources_used = []
    combined_input = ""

    # Wikipedia lookup
    wiki_result = wiki_lookup(request.query)
    if wiki_result:
        combined_input += wiki_result + "\n"
        sources_used.append("Wikipedia")

    # DuckDuckGo lookup
    ddg_result = ddg_lookup(request.query)
    if ddg_result:
        combined_input += ddg_result + "\n"
        sources_used.append("DuckDuckGo")

    prompt_text = f"""
You are a research assistant.

Use the research notes below to produce a concise factual summary.

Question:
{request.query}

Research Notes:
{combined_input}

Instructions:
- Write a short informative paragraph
- Do NOT ask follow-up questions
- Do NOT add conversational text
- Only provide the summary
"""

    # Ollama call
    # Ollama call
    try:
        response = chat(
            model="gemma3:4b",
            messages=[{"role": "user", "content": prompt_text}]
        )
        summary = response["message"]["content"]

    except Exception as e:
        print(e)
        summary = "Error generating AI response."
        # Save to file
        save_to_txt(f"Query: {request.query}\nSummary: {summary}")

    return ResearchResponse(topic=request.query, summary=summary, sources=sources_used)