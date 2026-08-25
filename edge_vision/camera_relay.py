import cv2
import torch
import os
import urllib.request
import urllib.parse
from ultralytics import YOLO

device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"🚀 TeerthMitra Edge Vision Active on: {device.upper()}")

current_dir = os.path.dirname(__file__)
sample_video = os.path.join(current_dir, "streams", "crowd_sample.mp4")

# Automatically download or load weights
model = YOLO("yolov8n.pt")

def stream_feed(source=sample_video):
    cap = cv2.VideoCapture(source if os.path.exists(source) else 0)
    frame_counter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            if isinstance(source, str):
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            break

        frame_counter += 1
        results = model.track(frame, persist=True, classes=[0], tracker="bytetrack.yaml", device=device, verbose=False)
        boxes = results[0].boxes
        person_count = len(boxes) if boxes is not None else 0

        if frame_counter % 10 == 0:
            try:
                params = urllib.parse.urlencode({
                    "temple_id": "somnath",
                    "zone_id": "Sanctum_Exit",
                    "count": person_count
                })
                url = f"http://127.0.0.1:8000/api/update-live-density?{params}"
                req = urllib.request.Request(url, method="POST")
                urllib.request.urlopen(req, timeout=0.2)
            except Exception:
                pass

        if person_count < 3:
            status, color = "SAFE (GREEN)", (0, 255, 0)
        elif person_count < 6:
            status, color = "CAUTION (YELLOW)", (0, 255, 255)
        else:
            status, color = "CRITICAL (RED)", (0, 0, 255)

        if boxes is not None and boxes.id is not None:
            track_ids = boxes.id.int().cpu().tolist()
            xyxy = boxes.xyxy.cpu().numpy()
            for box, track_id in zip(xyxy, track_ids):
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"ID:{track_id}", (x1, max(15, y1 - 5)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.rectangle(frame, (15, 15), (580, 65), (20, 20, 20), -1)
        cv2.putText(frame, f"Zone: Sanctum Exit | Count: {person_count} | {status}",
                    (25, 48), cv2.FONT_HERSHEY_SIMPLEX, 0.60, color, 2)

        cv2.imshow("TeerthMitra CCTV Telemetry Feed", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    stream_feed()
    