import cv2
import numpy as np

def draw_bounding_boxes(image, net, output_layers):
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
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = f"{class_ids[i]}: {confidences[i]:.2f}"
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    return image  # Return the image with bounding boxes drawn

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
unconnected_out_layers = net.getUnconnectedOutLayers()
if unconnected_out_layers.ndim == 2:
    output_layers = [layer_names[i[0] - 1] for i in unconnected_out_layers]
else:
    output_layers = [layer_names[i - 1] for i in unconnected_out_layers]

# Load images
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

# Draw bounding boxes on images
image1_with_boxes = draw_bounding_boxes(image1, net, output_layers)
image2_with_boxes = draw_bounding_boxes(image2, net, output_layers)

# Save or display the images
cv2.imwrite("image1_with_boxes.jpg", image1_with_boxes)
cv2.imwrite("image2_with_boxes.jpg", image2_with_boxes)

# Optionally display the images
# cv2.imshow("Image 1", image1_with_boxes)
# cv2.imshow("Image 2", image2_with_boxes)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
