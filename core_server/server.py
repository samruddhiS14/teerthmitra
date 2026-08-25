from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from core_server.routes.telemetry import router as telemetry_router
from core_server.routes.reservations import router as reservations_router
from core_server.routes.chatbot import router as chatbot_router

app = FastAPI(title="TeerthMitra — Autonomous Pilgrimage Grid")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "web_portal"))
app.mount("/static", StaticFiles(directory=static_path), name="static")

app.include_router(telemetry_router)
app.include_router(reservations_router)
app.include_router(chatbot_router)

@app.get("/", response_class=HTMLResponse)
def serve_portal():
    html_file = os.path.join(static_path, "index.html")
    with open(html_file, "r") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("core_server.server:app", host="127.0.0.1", port=8000, reload=True)