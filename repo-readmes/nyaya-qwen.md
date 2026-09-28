# ⚖️ NYAYA-QWEN: Offline Source-Grounded Legal RAG

A local, privacy-first Retrieval-Augmented Generation (RAG) system engineered to answer Indian legal questions strictly from loaded, verified legal corpora.

[![Ollama](https://img.shields.io/badge/LLM-Ollama%20Qwen3%3A8B-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Constitution](https://img.shields.io/badge/Corpus-Constitution%20of%20India-orange?style=for-the-badge)](https://legislative.gov.in)

---

## 🛡️ Core Tenet: Strict Citation-Grounded Synthesis

> **Never invent Article numbers, Section numbers, Acts, cases, punishments, procedures, dates, or legal citations.**

NYAYA-QWEN operates under rigorous guardrails:
1. **Source Constraint**: The language model is forbidden from answering beyond explicitly retrieved passages.
2. **Deterministic Citation Verification** (`citation_checker.py`): Every cited `pdf_page` number and statutory clause is verified post-inference against the retrieved set before the answer is returned to the user.
3. **100% Offline & Sovereign**: Operates on local hardware via Ollama `qwen3:8b`. Zero data leaves the machine.

---

## ✨ Features

- **400+ Pages Indexed**: Comprehensive indexing of the complete Constitution of India with pre-computed embeddings.
- **Multi-Stage Query Pipeline**: Query classification -> Domain expansion -> Dense retrieval -> LLM synthesis -> Automated citation validation.
- **Explicit Fallback Mode**: If retrieved documents cannot answer a question, the system clearly states what statutory references are absent rather than hallucinating.

---

## 🚀 Getting Started

### 1. Prerequisites
Install [Ollama](https://ollama.ai) and pull the target model:
```bash
ollama pull qwen3:8b
ollama serve
```

### 2. Installation & Run
```bash
git clone https://github.com/Demmonics/NYAYA-QWEN.git
cd NYAYA-QWEN

pip install -r requirements.txt
python main.py
```

---

## 📄 License
Developed for academic & research evaluation by [Yoosha Abbas](https://github.com/Demmonics).
