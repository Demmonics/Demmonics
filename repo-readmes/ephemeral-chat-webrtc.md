# ⚡ Ephemeral Peer-to-Peer Encrypted Chat

A zero-knowledge, serverless ephemeral chat platform utilizing **WebRTC Data Channels** and **AES-256-GCM** client-side encryption. Messages never touch a database and self-destruct upon session termination.

[![WebRTC](https://img.shields.io/badge/WebRTC-P2P-333333?style=for-the-badge&logo=webrtc&logoColor=white)](https://webrtc.org/)
[![Cryptography](https://img.shields.io/badge/Crypto-AES--256--GCM-green?style=for-the-badge)](https://en.wikipedia.org/wiki/Galois/Counter_Mode)
[![React](https://img.shields.io/badge/React%2018-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)

---

## 🔒 Cryptographic Model

1. **Direct Peer Data Channels**: Once WebRTC handshaking is completed via temporary signaling, all chat text, files, and voice notes travel peer-to-peer.
2. **Client-Side Key Derivation**: Encryption keys are derived in the browser using PBKDF2 with SHA-256 and never transmitted to the signaling server.
3. **Zero Persistence**: Refreshing the browser or severing the connection immediately erases cryptographic state from volatile RAM.

---

## 🛠️ Stack & Technologies

- **Frontend**: Vite, React, TypeScript, Tailwind CSS
- **Networking**: WebRTC `RTCDataChannel`, simple signaling WebSocket
- **Cryptography**: Web Crypto API (SubtleCrypto)

---

## 🚀 Quickstart

```bash
git clone https://github.com/Demmonics/ephemeral-chat.git
cd ephemeral-chat

npm install
npm run dev
```

---

## 📄 License
MIT License. Created by [Yoosha Abbas](https://github.com/Demmonics).
