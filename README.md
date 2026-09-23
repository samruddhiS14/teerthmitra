# TeerthMitra 

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Edge%20Vision-00FFFF)](https://ultralytics.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**TeerthMitra** is an edge-computed autonomous pilgrimage safety and crowd resilience platform engineered to protect heritage temple complexes during high-density festival surges. 

By unifying on-device YOLOv8 spatial tracking, real-time GIS digital twin telemetry, slot-balanced digital E-passes, zero-cellular offline emergency tethering, and a dedicated **TeerthSeva AI** guide, TeerthMitra eliminates stampede hazards before they form while ensuring smooth, dignified darshan for all pilgrims.

---

## Key Features

* **Edge Vision Telemetry:** Real-time crowd density ($p/m^2$) computation and ByteTrack spatial tracking processed locally without shipping raw video to external clouds.
* **GIS Digital Twin:** Dynamic spatial mapping over iconic Indian shrines (*Somnath, Dwarkadhish, Ambaji, Pavagadh*) with active chokepoint alerting and one-click proactive flow rerouting.
* **Smart E-Pass Desk:** Darshan time-slot balancing with OTP verification, automated priority allocation for elderly/differently-abled pilgrims, and downloadable PDF passes.
* **Zero-Network Tether:** Offline QR wristband registry designed to reunite lost children and guardians during severe festival cellular blackouts.
* **TeerthSeva AI:** Integrated AI assistant providing real-time shrine timings, accessible routes, and safety protocols.

---

## Tech Stack & Architecture

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Edge Computer Vision** | `YOLOv8n`, `ByteTrack`, `OpenCV`, `PyTorch` | Real-time object detection, spatial centroid tracking, and local crowd density ($p/m^2$) computation on Apple Silicon (MPS) / CUDA. |
| **Backend Core** | `FastAPI`, `Uvicorn`, `Pydantic` | High-throughput asynchronous REST API for telemetry ingestion, zone risk calculation, and E-pass tokenization. |
| **Pilgrim AI Assistant** | `Google Gemini 2.5 Flash`, `Python Requests` | Multilingual conversational intelligence for real-time darshan timings, accessible ramps, and safety guidance with offline semantic fallback. |
| **GIS & Digital Twin** | `Leaflet.js`, `OpenStreetMap API` | Real-time interactive spatial twin visualizing dynamic chokepoints and automated crowd rerouting paths across shrines. |
| **Frontend & UX** | `Tailwind CSS`, `Lucide Icons`, `JavaScript (ES6+)` | Responsive 5-tab command center and public access portal with client-side state management. |
| **Offline Safety & Utilities** | `QRCode.js`, `html2pdf.js`, `Web Speech API` | Zero-cellular emergency wristband resolution, scannable offline E-passes, client-side PDF export, and browser voice navigation. |

---

### Badges & Tools

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=leaflet&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

---

## Repository Structure

```text
TeerthMitra/
├── edge_vision/              # Local computer vision pipeline
│   ├── streams/              # Video benchmarks
│   ├── weights/              # Model weights (YOLOv8)
│   └── camera_relay.py       # Detection, tracking, & backend push script
├── core_server/              # Unified FastAPI backend
│   ├── routes/               # API endpoints (Telemetry, Booking, AI Assistant)
│   ├── state/                # Multi-shrine geospatial & booking registry
│   └── server.py             # ASGI application entrypoint
├── web_portal/               # Command center & pilgrim portal
│   ├── assets/               # Brand & shrine imagery
│   └── index.html            # 5-tab responsive GIS web application
├── requirements.txt          # Python dependencies
└── .gitignore                # Ignored cache & binary files
