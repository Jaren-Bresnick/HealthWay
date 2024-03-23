import food_recognition
from motion_recognition import detect_and_track_object

# Call the function with the relative path to the image file

image_paths = ["images/bottle1.jpg", "images/bottle2.jpg"]
food_recognition.main(image_paths[0])
direction = detect_and_track_object(image_paths)
print(direction)

