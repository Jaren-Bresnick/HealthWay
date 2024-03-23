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

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()

# Fix for the IndexError
out_layer_indexes = net.getUnconnectedOutLayers().flatten()
output_layers = [layer_names[i - 1] for i in out_layer_indexes]

# Load images
image1 = cv2.imread("images/bottle1.jpg")
image2 = cv2.imread("images/bottle2.jpg")

# Draw bounding boxes on images and detect main object
image1_with_boxes, position1 = draw_bounding_boxes_and_detect_object(image1, net, output_layers)
image2_with_boxes, position2 = draw_bounding_boxes_and_detect_object(image2, net, output_layers)

# Save the images with bounding boxes
cv2.imwrite("images/image1_with_boxes.jpg", image1_with_boxes)
cv2.imwrite("images/image2_with_boxes.jpg", image2_with_boxes)

# Determine direction
if position1 is not None and position2 is not None:
    direction = "The object moves from left to right." if position2 > position1 else "The object moves from right to left."
else:
    direction = "Could not determine the object's direction."

print(direction)

# Optionally display the images
# cv2.imshow("Image 1", image1_with_boxes)
# cv2.imshow("Image 2", image2_with_boxes)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
