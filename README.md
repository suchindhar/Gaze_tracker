# <div align="center">🧠 NeuroTrack</div>

<div align="center">

### **Real-Time Cognitive State & Attention Analyzer**

*AI-powered gaze tracking, head pose estimation, and fatigue detection with a unified Attention Score and intelligent OS automation.*

<img src="assets/hud_mockup.png" width="420" alt="NeuroTrack HUD"/>

<br>

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/MediaPipe-0.10.8-green?style=for-the-badge&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-4.8-lightgrey?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-Latest-orange?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Windows-OS%20Automation-0078D6?style=for-the-badge&logo=windows&logoColor=white"/>

</div>

---

# 🚀 Overview

NeuroTrack is an AI-powered computer vision system that estimates a user's cognitive attention level in real time using only a standard webcam.

Instead of relying on expensive eye-tracking hardware, NeuroTrack combines facial landmarks, gaze estimation, head pose analysis, and blink detection to generate a smooth **Attention Score (0–100)**. The system then performs intelligent desktop automation such as pausing media when user attention drops below a configurable threshold.

The project is designed using a modular object-oriented architecture, making it easy to extend with additional attention metrics, machine learning models, or productivity integrations.

---

# ✨ Features

* 🎯 Real-time gaze estimation
* 👀 Eye Aspect Ratio (EAR) fatigue detection
* 🙂 478-point facial landmark tracking
* 🧭 Head pose estimation (Yaw & Pitch)
* 📊 Continuous Attention Score (0–100)
* ⚡ Exponential smoothing for stable predictions
* 🖥️ Live OpenCV HUD
* ⌨️ Windows media control automation
* 🧩 Modular OOP architecture
* 📈 Low-latency real-time inference

---

# 🏗️ System Architecture

<div align="center">
<img src="assets/architecture.png" width="750"/>
</div>

```text
 Webcam
    │
    ▼
MediaPipe Face Mesh
(478 Facial Landmarks)
    │
    ├──────────────┐
    │              │
    ▼              ▼
Gaze Tracker    Head Pose Tracker
    │              │
    └──────┬───────┘
           │
           ▼
Fatigue Tracker
(Eye Aspect Ratio)
           │
           ▼
Attention Engine
(Exponential Smoothing)
           │
    ┌──────┴───────────┐
    ▼                  ▼
HUD Renderer      OS Controller
(OpenCV UI)      (Media Pause/Play)
```

---

# 🧠 Attention Scoring Pipeline

The final Attention Score is computed by combining multiple real-time cognitive indicators:

* Eye gaze direction
* Head orientation
* Eye Aspect Ratio (EAR)
* Blink frequency
* Temporal smoothing

Instead of making frame-by-frame decisions, NeuroTrack uses exponential smoothing to reduce noise and produce stable, reliable attention estimates.

---

# 🛠️ Technology Stack

| Category            | Technologies        |
| ------------------- | ------------------- |
| Language            | Python 3.11         |
| Computer Vision     | OpenCV              |
| Landmark Detection  | MediaPipe Face Mesh |
| Numerical Computing | NumPy               |
| Automation          | PyAutoGUI           |
| Rendering           | OpenCV GUI          |
| Platform            | Windows             |

---

# 📂 Project Structure

```text
NeuroTrack/
│
├── assets/
│   ├── hud_mockup.png
│   ├── architecture.png
│ 
│
├── src/
│   ├── gaze_tracker.py
│   ├── pose_tracker.py
│   ├── fatigue_tracker.py
│   ├── attention_engine.py
│   ├── hud_renderer.py
│   └── os_controller.py
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

```bash
git clone https://github.com/suchindhar/Gaze_tracker.git

cd Gaze_tracker

pip install -r requirements.txt

python app.py
```

---

# 📈 Future Improvements

* Face recognition support
* Personalized attention calibration
* Machine learning–based cognitive scoring
* Productivity analytics dashboard
* Session history and reporting
* Multi-monitor support
* Cross-platform automation
* REST API integration
* Edge AI optimization

---

# 🎯 Applications

* Online learning
* Workplace productivity
* Driver attention monitoring
* Human–computer interaction
* Smart classrooms
* AI-powered accessibility
* Research in cognitive computing

---

# 👨‍💻 Author

**Suchindhar**

* AI Engineer
* Machine Learning Engineer
* Computer Vision & Generative AI Enthusiast

GitHub: [**https://github.com/suchindhar**](https://github.com/suchindhar)

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🧠 Share your feedback and suggestions

---

<div align="center">

### **"Building AI systems that transform perception into intelligent action."**

</div>
