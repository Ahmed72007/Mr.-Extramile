"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query) return;
    setLoading(true);

    try {
      const res = await axios.post("http://localhost:8000/query", { query });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      setResult({ summary: "Error fetching data." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.title}>🤖 Mr. ExtraMile</h1>
        <p style={styles.subtitle}>Your Smart AI Research Assistant</p>

        <div style={styles.searchBox}>
          <input
            type="text"
            placeholder="Ask anything..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            style={styles.input}
          />

          <button onClick={handleSearch} style={styles.button}>
            🔍 Search
          </button>
        </div>

        {loading && (
          <div style={styles.loading}>
            <div style={styles.spinner}></div>
            <p>Mr. ExtraMile is researching...</p>
          </div>
        )}

        {result && (
          <div style={styles.resultCard}>
            <h3 style={styles.query}>📌 {result.topic}</h3>

            <p style={styles.summary}>{result.summary}</p>

            <div style={styles.sources}>
              {result.sources?.map((src: string, i: number) => (
                <span key={i} style={styles.sourceTag}>
                  {src}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

const styles: any = {

  page: {
    height: "100vh",
    background:
      "linear-gradient(135deg, #4f46e5, #9333ea, #ec4899)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    fontFamily: "system-ui",
  },

  card: {
    background: "white",
    padding: "40px",
    borderRadius: "16px",
    width: "650px",
    boxShadow: "0 15px 40px rgba(0,0,0,0.2)",
    textAlign: "center",
  },

  title: {
    fontSize: "36px",
    fontWeight: "700",
    marginBottom: "5px",
  },

  subtitle: {
    color: "#666",
    marginBottom: "30px",
  },

  searchBox: {
    display: "flex",
    gap: "10px",
  },

  input: {
    flex: 1,
    padding: "14px",
    borderRadius: "8px",
    border: "1px solid #ddd",
    fontSize: "16px",
  },

  button: {
    padding: "14px 20px",
    borderRadius: "8px",
    border: "none",
    background: "#6366f1",
    color: "white",
    fontWeight: "600",
    cursor: "pointer",
  },

  loading: {
    marginTop: "20px",
  },

  spinner: {
    width: "30px",
    height: "30px",
    border: "4px solid #eee",
    borderTop: "4px solid #6366f1",
    borderRadius: "50%",
    margin: "0 auto",
    animation: "spin 1s linear infinite",
  },

  resultCard: {
    marginTop: "30px",
    textAlign: "left",
    background: "#f9fafb",
    padding: "20px",
    borderRadius: "12px",
  },

  query: {
    marginBottom: "10px",
  },

  summary: {
    lineHeight: "1.6",
    color: "#333",
  },

  sources: {
    marginTop: "15px",
  },

  sourceTag: {
    background: "#e0e7ff",
    padding: "6px 10px",
    borderRadius: "6px",
    marginRight: "8px",
    fontSize: "13px",
  },
};