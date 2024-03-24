# file name: object_detection_and_tracking.py
import cv2
import numpy as np

def draw_bounding_boxes_and_detect_object(image, net, output_layers):
    height, width = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Confidence threshold
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    main_object_center_x = None
    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = f"{class_ids[i]}: {confidences[i]:.2f}"
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        if main_object_center_x is None or confidences[i] > main_object_center_x['confidence']:
            main_object_center_x = {'x_center': (x + w / 2) / width, 'confidence': confidences[i]}
    
    return image, main_object_center_x['x_center'] if main_object_center_x else None

def detect_and_track_object(image_paths):
    # Load YOLO
    net = cv2.dnn.readNet("/Users/shrisha/Desktop/FoodInventory/food_recognition/yolov3.weights", "/Users/shrisha/Desktop/FoodInventory/food_recognition/yolov3.cfg")
    layer_names = net.getLayerNames()

    # Fix for the IndexError
    out_layer_indexes = net.getUnconnectedOutLayers().flatten()
    output_layers = [layer_names[i - 1] for i in out_layer_indexes]

    results = []
    for image_path in image_paths:
        image = cv2.imread(image_path)
        processed_image, position = draw_bounding_boxes_and_detect_object(image, net, output_layers)
        results.append((processed_image, position))
        # Save the images with bounding boxes
        cv2.imwrite(image_path.replace('.jpg', '_with_boxes.jpg'), processed_image)

    # Determine direction
    if all(position is not None for _, position in results):
        #Assume sensor is on the right side
        direction = "In" if results[1][1] > results[0][1] else "Out"
    else:
        direction = "Could not determine the object's direction."

    return direction

# print(detect_and_track_object(["images/frame_1.jpg", "images/frame_2.jpg"]))  # Example usage