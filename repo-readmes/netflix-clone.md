# 🎬 MERN Streaming Application with Local Media Engine

A full-stack media streaming platform built on the MERN architecture (MongoDB, Express, React, Node.js), customized with a dedicated local media pipeline for serving and streaming high-bitrate video assets directly from local storage.

[![Tech Stack](https://img.shields.io/badge/Stack-MERN-green?style=for-the-badge)](https://github.com/Demmonics)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)

---

## 📸 Media Preview
<!-- PLACEHOLDER: Add demo screenshot or walkthrough GIF here -->
<!-- ![Streaming Platform UI](./screenshot.png) -->

---

## ⚡ Key Highlights & Features

- **Local Video Pipeline**: Custom Express static streaming controller supporting chunked `206 Partial Content` HTTP byte-range requests for seamless seeking.
- **Authentication & Sessions**: Secure JWT-based user authentication stored in encrypted HTTP-only cookies.
- **Dynamic Catalog**: Categorized movie and TV show exploration with search, genre filters, and trailer playback.
- **User Watchlist & History**: Dedicated database collections tracking viewing activity and user favorites.
- **Responsive Cinematic UI**: Styled with Tailwind CSS for desktop, tablet, and mobile viewing.

---

## 🛠️ Stack & Dependencies

- **Frontend**: React, React Router, Tailwind CSS, Axios, Lucide Icons
- **Backend**: Node.js, Express.js, JSON Web Tokens (`jsonwebtoken`), BcryptJS
- **Database**: MongoDB with Mongoose ODM

---

## 🚀 Setup & Execution

### 1. Environment Configuration
Create `.env` in the backend directory:
```env
PORT=5000
MONGO_URI=mongodb://localhost:27017/netflix_clone
JWT_SECRET=your_super_secret_jwt_key
NODE_ENV=development
```

### 2. Launch Backend
```bash
cd backend
npm install
npm run dev
```

### 3. Launch Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 📄 License
MIT License. Created by [Yoosha Abbas](https://github.com/Demmonics).
