# 1. YOLOv5n (nano) - Smallest YOLO variant (~2MB)
import torch
import cv2

def setup_object_detection():
    # Load directly from pytorch hub
    model = torch.hub.load('ultralytics/yolov5', 'yolov5n')  # nano model
    return model

def detect_objects(image_path):
    model = setup_object_detection()
    # Read image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Detect objects
    results = model(image_rgb)
    
    # Get detections
    detections = results.pandas().xyxy[0]
    
    # Draw boxes on image (for visualization)
    annotated_image = image.copy()
    for idx, detection in detections.iterrows():
        x1, y1, x2, y2 = int(detection['xmin']), int(detection['ymin']), int(detection['xmax']), int(detection['ymax'])
        label = f"{detection['name']} {detection['confidence']:.2f}"
        
        # Draw box
        cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Add label
        cv2.putText(annotated_image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return {
        'detections': detections,
    }

