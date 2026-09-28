# ⚖️ NYAYA-TRIAGE: Legal AI Triage & Case Analytics Platform

An enterprise-grade, multi-role legal intelligence platform designed for the **Smart India Hackathon (SIH)**. NYAYA-TRIAGE bridges the gap between Indian citizens and the justice system by combining hybrid vector-lexical legal retrieval with grounded reasoning pipelines.

[![Python](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-React%2019-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![Qdrant](https://img.shields.io/badge/Vector%20DB-Qdrant-DC382D?style=for-the-badge&logo=qdrant&logoColor=white)](https://qdrant.tech/)
[![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Supabase](https://img.shields.io/badge/Auth-Supabase%20JWKS-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

---

## 📸 Interface Preview
<!-- PLACEHOLDER: Insert dashboard / 3D Lady Justice demo GIF here -->
<!-- ![NYAYA Triage Dashboard](./preview.png) -->

---

## 🏛️ Core Architectural Pillars

```
┌─────────────────────────────────────────────────────────────────┐
│                      Client Layer (React 19)                    │
│   • 3D Lady Justice Viewport (Three.js WebGL)                   │
│   • Multi-Role Portal (Citizen / Lawyer / Judge / Admin)        │
│   • Asymmetric JWT Auth via Supabase JWKS                       │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FastAPI Reasoning Core                      │
│   • SentenceTransformers Local Embeddings (all-MiniLM-L6-v2)    │
│   • Qdrant Vector Semantic Retrieval                            │
│   • BM25 Lexical Keyword Retrieval via MongoDB                  │
│   • IPC-to-BNS Statutory Code Mapping                           │
│   • Grounded Synthesis via Gemini API with Page-Level Citations │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✨ Features & Capabilities

- **Role-Based Legal Dashboards**:
  - **Citizen**: Natural-language dispute submission, eligibility checks, plain-language legal explanation.
  - **Lawyer & Judge**: Case docket triage, automated bail and precedent search, statutory section linking.
  - **Admin**: Document ingestion pipeline, OCR processing, vector index status.
- **IPC-to-BNS Statutory Cross-Reference**: Automatic transliteration and section mapping between the Indian Penal Code (IPC) and the Bharatiya Nyaya Sanhita (BNS).
- **Zero-Hallucination Retrieval Pipeline**: Retrieved chunks from Indian Supreme Court precedents and the Constitution are formatted with explicit `pdf_page` markers.
- **Hybrid Retrieval System**: Combines 384-dimensional dense semantic vectors (Qdrant) with sparse BM25 lexical ranking for legal terms of art.

---

## 🛠️ Stack & Dependencies

- **Frontend**: React 19, Vite 8, Three.js, React Router 7, Tailwind CSS 4, Chart.js, `@supabase/supabase-js`
- **Backend**: Python 3.11+, FastAPI, Uvicorn, Pydantic v2, `google-genai`, `qdrant-client`, `pymongo`, `sentence-transformers`, `rank-bm25`, PyMuPDF, Tesseract OCR
- **Databases**: Qdrant Cloud / Docker, MongoDB (Precedent corpus & metadata), SQLite (Local history)

---

## 🚀 Setup & Development

### Backend Service
```bash
cd Backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
python -m uvicorn app.main:app --reload --port 8000
```
Interactive OpenAPI documentation: `http://localhost:8000/docs`

### Frontend Application
```bash
npm install
cp .env.example .env
npm run dev
```

---

## 📄 License
Confidential / Proprietary Hackathon Submission. Developed by [Yoosha Abbas](https://github.com/Demmonics) & Team.
