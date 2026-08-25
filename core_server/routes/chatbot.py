from fastapi import APIRouter
from pydantic import BaseModel
import os
import requests
from core_server.state.shrine_registry import shrine_data

router = APIRouter(prefix="/api", tags=["AI Pilgrim Assistant"])

class ChatRequest(BaseModel):
    message: str
    shrine: str = "somnath"

SYSTEM_PROMPT = """
You are 'TeerthSeva AI', an empathetic, helpful, and culturally respectful AI pilgrim assistant for the TeerthMitra platform.
You answer pilgrim queries regarding:
1. Temple darshan timings, morning/evening aarti schedules, and wait times.
2. Accessibility (wheelchair ramps, elderly priority access, battery shuttles).
3. Crowd safety tips, emergency SOS protocols, lost person desk (1094), and helpline (1800-11-2026).
4. Cultural & architectural heritage of Somnath, Dwarkadhish, Ambaji, and Pavagadh.

Keep your answers concise, clear, polite, and reassuring (under 3 sentences).
"""

def dynamic_local_response(query: str, shrine_key: str) -> str:
    """Intelligent semantic response engine for offline/fallback mode."""
    q = query.lower()
    temple = shrine_data.get(shrine_key.lower(), shrine_data["somnath"])
    name = temple["name"]
    wait = temple.get("wait_time", "25 mins")
    count = temple.get("headcount", 3400)

    if any(w in q for w in ["wait", "time", "queue", "how long", "rush", "crowd", "line"]):
        return f"The current estimated wait time at {name} is approximately {wait} with an active footfall of {count:,} pilgrims. Priority queues are active at Gate 1."
    
    if any(w in q for w in ["where", "location", "situated", "address", "reach", "city"]):
        return f"{name} is located in {temple['city']}, Gujarat. Navigational signage and parking shuttles are available at the main entry gates."

    if any(w in q for w in ["aarti", "darshan timing", "schedule", "open", "close"]):
        return f"Darshan at {name} is open daily from 6:00 AM to 10:00 PM. Morning Mangla Aarti is at 7:00 AM and Evening Sandhya Aarti is at 7:00 PM."

    if any(w in q for w in ["wheelchair", "elderly", "disabled", "ramp", "differently"]):
        return f"Accessible ramps and dedicated wheelchair assistance are available at Gate 1. Electric transit shuttles operate every 4 minutes."

    if any(w in q for w in ["lost", "sos", "emergency", "help", "police", "doctor"]):
        return "For immediate emergencies, press the red SOS button or dial 1800-11-2026. For lost persons, visit the Zero-Network Tether post (Call 1094)."

    return f"Namaste! I am TeerthSeva AI for {name}. You can ask me about queue wait times, darshan schedules, or wheelchair accessibility."

@router.post("/chat")
def chat_with_assistant(req: ChatRequest):
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    # If the key is absent or not a standard Google AI Studio key, use the local response engine
    if not api_key or not api_key.startswith("AIzaSy"):
        return {"reply": dynamic_local_response(req.message, req.shrine)}

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"{SYSTEM_PROMPT}\nActive Shrine: {req.shrine}\nPilgrim Question: {req.message}"}
                    ]
                }
            ]
        }
        resp = requests.post(url, json=payload, timeout=7)
        data = resp.json()

        if resp.status_code == 200 and "candidates" in data:
            return {"reply": data["candidates"][0]["content"]["parts"][0]["text"]}
        else:
            return {"reply": dynamic_local_response(req.message, req.shrine)}
    except Exception:
        return {"reply": dynamic_local_response(req.message, req.shrine)}