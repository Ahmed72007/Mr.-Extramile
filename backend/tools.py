# tools.py
import wikipedia
import requests
from datetime import datetime

def search_tool(query: str) -> str:
    """DuckDuckGo search."""
    try:
        res = requests.get(
            "https://api.duckduckgo.com/", 
            params={"q": query, "format": "json", "no_html": 1, "skip_disambig": 1}
        )
        data = res.json()
        return data.get("AbstractText") or "No DuckDuckGo result found."
    except:
        return "DuckDuckGo search failed."

def wiki_tool(query: str) -> str:
    """Wikipedia summary."""
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation, options: {e.options[:5]}"
    except:
        return "No Wikipedia page found."

def save_to_txt(text: str, filename="research_output.txt") -> str:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"--- {ts} ---\n{text}\n\n")
    return f"Saved to {filename}"