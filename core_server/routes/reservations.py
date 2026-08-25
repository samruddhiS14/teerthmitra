from fastapi import APIRouter
from pydantic import BaseModel
import random
import time

router = APIRouter(prefix="/api", tags=["Reservations"])

bookings = {}

class BookingRequest(BaseModel):
    temple: str
    group_lead: str
    phone: str = ""
    members_count: int
    slot_time: str
    priority_elderly: bool = False

@router.post("/book-pass")
def book_pass(req: BookingRequest):
    pass_id = f"TM-{req.temple[:3].upper()}-{random.randint(1000, 9999)}"
    bookings[pass_id] = {
        "pass_id": pass_id,
        "temple": req.temple,
        "slot": req.slot_time,
        "group_lead": req.group_lead,
        "phone": req.phone,
        "members": req.members_count,
        "priority_elderly": req.priority_elderly,
        "booked_at": time.time(),
    }
    return {"status": "Success", "pass_id": pass_id, **bookings[pass_id]}

@router.get("/bookings")
def list_bookings():
    return list(bookings.values())