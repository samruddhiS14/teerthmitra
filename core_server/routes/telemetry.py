from fastapi import APIRouter
from core_server.state.shrine_registry import shrine_data, wristbands

router = APIRouter(prefix="/api", tags=["Telemetry"])

@router.get("/temples")
def get_all_temples():
    return shrine_data

@router.get("/temple/{shrine_id}")
def get_shrine(shrine_id: str):
    return shrine_data.get(shrine_id.lower(), {"error": "Temple not found"})

@router.post("/update-live-density")
def update_live_density(temple_id: str, zone_id: str, count: int):
    if temple_id in shrine_data and zone_id in shrine_data[temple_id]["zones"]:
        target = shrine_data[temple_id]["zones"][zone_id]
        density = round(max(0.6, count * 0.8), 1)
        target["density"] = density
        target["risk"] = "Red" if density >= 4.0 else ("Yellow" if density >= 2.0 else "Green")
        target["status"] = "Critical" if density >= 4.0 else ("Caution" if density >= 2.0 else "Safe")
        return {"success": True, "updated": target}
    return {"error": "Target zone not found"}

@router.post("/simulate-reroute")
def reroute_zone(temple_id: str, zone_id: str):
    if temple_id in shrine_data and zone_id in shrine_data[temple_id]["zones"]:
        target = shrine_data[temple_id]["zones"][zone_id]
        target["density"] = 1.3
        target["status"] = "Safe (Diverted)"
        target["risk"] = "Green"
        return {"success": True, "updated": target}
    return {"error": "Zone not found"}

@router.get("/wristband/{band_id}")
def get_wristband(band_id: str):
    return wristbands.get(band_id, {"error": "Wristband not registered"})