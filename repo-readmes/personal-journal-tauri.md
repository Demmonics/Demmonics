# 📓 Chronos: Encrypted Offline-First Desktop Journal

A secure, private personal journaling application built with **Tauri v2**, **Rust**, and **React**. Engineered for long-term data sovereignty with zero cloud dependency and automated local backup rotation.

[![Tauri](https://img.shields.io/badge/Tauri-v2-FFC131?style=for-the-badge&logo=tauri&logoColor=black)](https://tauri.app/)
[![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![React](https://img.shields.io/badge/React%20%2B%20TS-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

---

## 📸 Interface Preview
<!-- PLACEHOLDER: Insert desktop application screenshot here -->
<!-- ![Desktop Journal UI](./preview.png) -->

---

## 🔒 Security & Offline Architecture

- **True Data Sovereignty**: 100% of journal entries and attachments are stored locally on disk in a persistent SQLite database (`diary.db`).
- **Automated Rolling Backup Engine**: Embedded Rust background job creates automated timestamped backups on write (`backups/diary/backup-YYYY-MM-DD-HHhMM.db`), preventing accidental data loss.
- **Client-Side Encryption**: Sensitive thoughts encrypted at rest before serialization.
- **Native OS Footprint**: Sub-30MB memory consumption enabled by Tauri's native webview architecture.

---

## 🛠️ Stack & Dependencies

- **Desktop Framework**: Tauri v2
- **Backend Systems**: Rust, `rusqlite` / SQLite, `serde`
- **Frontend Layer**: React, TypeScript, Tailwind CSS, TipTap / Markdown Editor

---

## 🚀 Development Setup

### Prerequisites
- [Rust Toolchain](https://rustup.rs/)
- [Node.js](https://nodejs.org/)

```bash
# Install frontend dependencies
npm install

# Run application in development mode with hot-reload
npm run tauri dev

# Compile release binary for Windows / macOS / Linux
npm run tauri build
```

---

## 📄 License
Personal & Private Project by [Yoosha Abbas](https://github.com/Demmonics).
