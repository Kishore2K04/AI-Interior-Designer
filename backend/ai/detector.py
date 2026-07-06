from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_room(image_path):
    results = model(image_path)

    detected_objects = []

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            detected_objects.append(model.names[class_id])

    return list(set(detected_objects))