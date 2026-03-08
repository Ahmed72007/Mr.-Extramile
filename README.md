
# Mr. ExtraMile – AI Research Assistant
<img width="1366" height="654" alt="image" src="https://github.com/user-attachments/assets/d9ddd9d2-e58c-46d2-b742-afc1fcd13441" />

**Project Status:** Proof-of-Concept / Idea Execution

Mr. ExtraMile is a focused AI-powered research assistant designed to help users get concise summaries and references for any query by combining local search results and large language model processing. This is not a finished product but a working demonstration of how an AI research tool can be implemented.

---

## **Project Overview**

Mr. ExtraMile accepts a user query, performs background research using online sources, and generates a human-like summary using AI. The project is structured to separate backend AI processing from a modern frontend interface.

### **Key Functionalities Implemented**

1. **Multi-Source Querying**

   * **Wikipedia Lookup**: Extracts the first few sentences of a Wikipedia article for the given query using the `wikipedia` Python library.
   * **DuckDuckGo Scraping**: Collects text snippets from DuckDuckGo search results using the `ddgs` library.
   * These sources are combined into a single context for AI summarization.

2. **Local LLM Integration (Ollama)**

   * Uses the **Ollama Python client** (`ollama`) to send queries to a local LLM (`gemma3:4b`) for generating a human-readable summary.
   * This avoids dependency on external cloud APIs and keeps computation local.
   * The AI summarizes the combined context from Wikipedia and DuckDuckGo to give concise insights.

3. **Custom Research Response Structure**

   * The backend defines a Pydantic model `ResearchResponse`:

     ```python
     class ResearchResponse(BaseModel):
         topic: str
         summary: str
         sources: List[str]
     ```
   * This ensures that every response contains:

     * The original query (`topic`)
     * The AI-generated summary (`summary`)
     * The list of sources used (`sources`)

4. **Frontend Implementation (Next.js)**

   * Modern, responsive interface built in **React + Next.js**.
   * Supports:

     * Query input box
     * AI-generated summary display
     * List of sources
     * Loading state feedback
   * Lightweight design with a named AI persona: **“Mr. ExtraMile”**.
   * Fully client-side, interacting with the backend via Axios API requests.

5. **File Logging**

   * All research queries and AI responses are saved locally in `research_output.txt` for record-keeping and debugging purposes.
   * Timestamped entries help in reviewing previous queries.

---

## **Implementation Notes**

* **Backend:** FastAPI handles API routing and integrates multiple sources of data with LLM summarization.
* **Frontend:** Next.js provides a modern, interactive interface for user queries.
* **LLM Choice:** Ollama is used locally to avoid exposing API keys and to maintain a lightweight AI environment.
* **Security:** `.env` files with sensitive data (like API keys) are excluded from the repository to comply with GitHub push protection rules.

---

## **Limitations / Not Finished**

* This project is a **prototype** / idea execution, not a production-ready product.
* AI outputs depend entirely on local LLM capability (`gemma3:4b`) and the quality of retrieved snippets.
* No authentication, caching, or large-scale optimization is implemented yet.
* Future improvements could include:

  * Adding more reliable sources
  * Context-aware prompt engineering
  * Saving query history in a database
  * Supporting multiple LLM backends

---

## **How to Run**

1. Clone the repository
2. Install Python and Node.js dependencies:

   ```bash
   pip install -r backend/requirements.txt
   cd frontend
   npm install
   npm run dev
   ```
3. Run FastAPI backend:

   ```bash
   uvicorn backend.main:app --reload
   ```
4. Open frontend in browser (`http://localhost:3000`) and start querying!

---

## **Conclusion**

Mr. ExtraMile demonstrates how combining multi-source research with a local LLM can produce concise AI-assisted summaries. It is a **proof-of-concept idea executed successfully**, showcasing:

* AI integration with Ollama
* FastAPI backend for research aggregation
* Modern React/Next.js frontend for user interaction

This project is a starting point for anyone interested in building AI-powered research assistants.

