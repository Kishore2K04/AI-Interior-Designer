from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_room(image_path):
    results = model(image_path)

    objects = []

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            objects.append({
                "name": model.names[class_id],
                "x": int(x1),
                "y": int(y1),
                "width": int(x2 - x1),
                "height": int(y2 - y1)
            })

    return objects