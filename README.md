<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1E90FF,100:9D4EDD&height=220&section=header&text=NeuroTrack&fontSize=65&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Real-Time%20Cognitive%20State%20%26%20Attention%20Analyzer&descAlignY=55&descAlign=50&descColor=e0e0e0" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=22&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=%F0%9F%91%80+AI-Powered+Gaze+Tracking;%F0%9F%A7%AD+Head+Pose+Estimation;%E2%9A%A1+Fatigue+%26+Blink+Detection;%F0%9F%93%8A+Real-Time+Attention+Scoring;%F0%9F%96%A5%EF%B8%8F+Intelligent+OS+Automation" alt="Typing SVG" />

<br>

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/MediaPipe-0.10.8-00B86B?style=for-the-badge&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-4.8-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-Latest-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Windows-OS%20Automation-0078D6?style=for-the-badge&logo=windows&logoColor=white"/>

<br>

<img src="https://img.shields.io/github/stars/suchindhar/Gaze_tracker?style=for-the-badge&logo=github&color=FFD700&labelColor=1a1a1a"/>
<img src="https://img.shields.io/github/forks/suchindhar/Gaze_tracker?style=for-the-badge&logo=github&color=32CD32&labelColor=1a1a1a"/>
<img src="https://img.shields.io/github/last-commit/suchindhar/Gaze_tracker?style=for-the-badge&color=blue&labelColor=1a1a1a"/>
<img src="https://img.shields.io/github/repo-size/suchindhar/Gaze_tracker?style=for-the-badge&color=orange&labelColor=1a1a1a"/>

</div>

<br>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#%EF%B8%8F-preview">Preview</a> •
  <a href="#%EF%B8%8F-architecture">Architecture</a> •
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## 🚀 Overview

**NeuroTrack** is an AI-powered computer vision system that estimates a user's cognitive attention level in real time — using nothing more than a standard webcam.

Instead of relying on expensive dedicated eye-tracking hardware, NeuroTrack fuses facial landmarks, gaze estimation, head pose analysis, and blink detection into a single, smooth **Attention Score (0–100)**. When focus drops below a configurable threshold, it can trigger intelligent desktop automation — like pausing your media automatically.

Built with a modular, object-oriented architecture so it's easy to extend with new attention metrics, ML models, or productivity integrations.

---

## ✨ Features

<table>
<tr>
<td width="50%">

🎯 **Real-time gaze estimation**
Tracks eye direction frame-by-frame

👀 **EAR fatigue detection**
Eye Aspect Ratio-based drowsiness signal

🙂 **478-point facial landmarks**
Powered by MediaPipe Face Mesh

🧭 **Head pose estimation**
Yaw & pitch tracking for orientation

</td>
<td width="50%">

📊 **Continuous Attention Score**
Unified 0–100 focus metric

⚡ **Exponential smoothing**
Stable, noise-resistant predictions

🖥️ **Live OpenCV HUD**
Real-time on-screen overlay

⌨️ **Windows automation**
Auto media pause/play on distraction

</td>
</tr>
</table>

---

## 🖥️ Preview

<div align="center">
<img src="assests/hud_mockup.png" width="480" alt="NeuroTrack HUD Preview"/>

<sub>Live HUD overlay — no demo video yet, but a GIF/clip is on the way. ⭐ Star the repo to get notified.</sub>
</div>

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[📷 Webcam] --> B[MediaPipe Face Mesh<br/>478 Facial Landmarks]
    B --> C[Gaze Tracker]
    B --> D[Head Pose Tracker]
    C --> E[Fatigue Tracker<br/>Eye Aspect Ratio]
    D --> E
    E --> F[Attention Engine<br/>Exponential Smoothing]
    F --> G[🖥️ HUD Renderer<br/>OpenCV UI]
    F --> H[⚙️ OS Controller<br/>Media Pause/Play]

    style A fill:#1E90FF,color:#fff
    style F fill:#9D4EDD,color:#fff
    style G fill:#00B86B,color:#fff
    style H fill:#FF6B6B,color:#fff
```

<details>
<summary>📈 Attention Scoring Pipeline</summary>
<br>

The final Attention Score is computed by combining multiple real-time cognitive indicators:

- Eye gaze direction
- Head orientation
- Eye Aspect Ratio (EAR)
- Blink frequency
- Temporal smoothing

Rather than making frame-by-frame decisions, NeuroTrack applies exponential smoothing to reduce noise and produce stable, reliable attention estimates.

</details>

---

## 🛠️ Tech Stack

<div align="center">
<img src="https://skillicons.dev/icons?i=python,opencv,windows,git,github&theme=dark" />
</div>

<br>

| Category | Technologies |
|---|---|
| Language | Python 3.11 |
| Computer Vision | OpenCV |
| Landmark Detection | MediaPipe Face Mesh |
| Numerical Computing | NumPy |
| Automation | PyAutoGUI |
| Rendering | OpenCV GUI |
| Platform | Windows |

---

## 📂 Project Structure

```text
Gaze_tracker/
│
├── analyzer/          # Core gaze, pose & fatigue analysis logic
├── assests/           # Images, mockups & architecture diagrams
├── models/             # ML / landmark model files
├── ui/                  # HUD & UI rendering components
├── venv/                # Virtual environment (local, not committed)
│
├── Documentation.pdf   # Project documentation
├── main.py              # Application entry point
├── requirements.txt    # Python dependencies
└── README.md
```

> ℹ️ Adjust this tree if `analyzer/`, `models/`, or `ui/` contain subfolders you'd like called out explicitly.

---

## ⚙️ Installation

```bash
git clone https://github.com/suchindhar/Gaze_tracker.git
cd Gaze_tracker

pip install -r requirements.txt
python main.py
```

---

## 🗺️ Roadmap

- [ ] Face recognition support
- [ ] Personalized attention calibration
- [ ] Machine learning–based cognitive scoring
- [ ] Productivity analytics dashboard
- [ ] Session history & reporting
- [ ] Multi-monitor support
- [ ] Cross-platform automation
- [ ] REST API integration
- [ ] Edge AI optimization

---

## 🎯 Applications

<div align="center">

| 🎓 Online Learning | 💼 Workplace Productivity | 🚗 Driver Monitoring |
|:---:|:---:|:---:|
| **🖥️ HCI Research** | 🏫 Smart Classrooms | ♿ AI Accessibility |

</div>

---

## 👨‍💻 Author

<div align="center">

**Suchindhar**
*AI Engineer · Machine Learning Engineer · Computer Vision & Generative AI Enthusiast*

<img src="https://img.shields.io/badge/GitHub-suchindhar-181717?style=for-the-badge&logo=github&logoColor=white"/>

</div>

---

## ⭐ Support

If this project helped or interested you:

⭐ **Star** the repository · 🍴 **Fork** it · 🧠 **Share feedback**

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:9D4EDD,100:1E90FF&height=120&section=footer"/>

### *"Building AI systems that transform perception into intelligent action."*

</div>
