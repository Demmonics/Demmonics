# ♟️ Grandmaster AI: Offline Chess Engine & Tactics Coach

An interactive, completely offline chess training environment equipped with a verified bitboard move generator, Minimax AI engine with alpha-beta pruning, and curated tactics puzzles.

[![Chess](https://img.shields.io/badge/Chess-AI%20Engine-black?style=for-the-badge&logo=lichess&logoColor=white)](https://github.com/Demmonics)
[![Algorithms](https://img.shields.io/badge/Algorithm-Minimax%20%2B%20Alpha--Beta-blue?style=for-the-badge)](https://en.wikipedia.org/wiki/Minimax)
[![Offline](https://img.shields.io/badge/Mode-100%25%20Offline-orange?style=for-the-badge)](https://github.com/Demmonics)

---

## 🎯 Engine & Training Architecture

- **Deterministic Rule Verification**: Full implementation of FIDE chess rules including en-passant, castling rights, promotion, and threefold repetition.
- **Evaluation Heuristics**: Piece-square tables, pawn structure evaluation, king safety penalties, and mobility scoring.
- **Adaptive Minimax**: Variable search depth with alpha-beta pruning and quiescence search to mitigate horizon effect.
- **Tactics Curriculum**: Step-by-step puzzle trainer diagnosing forks, pins, skewers, and discovered checks.

---

## 🛠️ Stack

- **Core**: JavaScript / TypeScript / WebAssembly
- **State**: Custom Bitboard / FEN Parser
- **Interface**: Responsive interactive canvas with move annotations

---

## 🚀 Usage

```bash
git clone https://github.com/Demmonics/chess-teaching-app.git
cd chess-teaching-app

npm install
npm run dev
```

---

## 📄 License
MIT License. Created by [Yoosha Abbas](https://github.com/Demmonics).
