# 💻 Apple MacBook Pro 3D Showcase (GSAP + Three.js)

An interactive, high-fidelity 3D product landing page for the Apple MacBook Pro, combining photorealistic WebGL rendering with kinetic scroll-driven GSAP animations.

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Preview-00f0ff?style=for-the-badge&logo=vercel&logoColor=white)](https://demmonics.github.io)
[![Three.js](https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=white)](https://threejs.org/)
[![GSAP](https://img.shields.io/badge/GSAP-88CE02?style=for-the-badge&logo=greensock&logoColor=white)](https://greensock.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

---

## 📸 Media Preview
<!-- PLACEHOLDER: Add recording / demo GIF here -->
<!-- ![MacBook 3D Demo](./preview.gif) -->

---

## ✨ Features

- **Interactive 3D Viewport**: Seamless 360-degree model inspection powered by `@react-three/fiber` and `@react-three/drei`.
- **GSAP ScrollTrigger Choreography**: Camera dolly zoom, lid opening/closing, and feature callouts tied smoothly to page scroll position.
- **Hardware Finish Configurator**: Instant real-time material swapping between Space Black and Silver finishes.
- **Micro-Animations & Kinetic Typography**: Smooth text reveal masks and responsive layout matching Apple's design language.
- **Performance Optimized**: Model level-of-detail (LOD), Draco geometry compression, and adaptive pixel ratios to maintain 60 FPS on mobile and desktop.

---

## 🛠️ Architecture & Tech Stack

- **Framework**: React 18 / 19 with Vite 5
- **3D Graphics**: Three.js, React Three Fiber, React Three Drei
- **Animation**: GSAP (GreenSock), ScrollTrigger
- **Styling**: Tailwind CSS
- **State Management**: Zustand / React state

---

## 🚀 Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/Demmonics/Apple-macbook-landing-page.git
cd Apple-macbook-landing-page

# 2. Install dependencies
npm install

# 3. Start development server
npm run dev

# 4. Build for production
npm run build
```

---

## 📄 License
MIT License. Created by [Yoosha Abbas](https://github.com/Demmonics).
