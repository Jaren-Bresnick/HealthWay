import cv2
import sys 
import os 
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../food_recognition'))
import motion_recognition

def extract_frames(video_path, output_path, frame_count=10):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Calculate frame indices for extraction
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_indices = [int(i * total_frames / (frame_count + 1)) for i in range(1, frame_count + 1)]

    extracted_frames = []
    # Extract frames
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            extracted_frames.append(frame)
        else:
            print(f"Error: Could not read frame {idx}")

    # Write extracted frames to files
    for i, frame in enumerate(extracted_frames):
        output_file = os.path.join(output_path, f"frame_{i+1}.jpg")
        cv2.imwrite(output_file, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])  # Set JPEG quality to 100%

    # Release the video capture object
    cap.release()

# Define paths
video_path = "video.mp4"
output_path = "output_frames"
frames_to_analyze_path = "frames_to_analyze"
extract_frames(video_path, output_path, frame_count=7)  # Collect 10 frames

# Get the paths of the extracted frames
frame_files = sorted([os.path.join(output_path, f) for f in os.listdir(output_path) if f.endswith('.jpg')])

# Create directory to store frames to analyze if it doesn't exist
if not os.path.exists(frames_to_analyze_path):
    os.makedirs(frames_to_analyze_path)

# Move the selected frames to the frames_to_analyze directory
for i, idx in enumerate([3,7], start=1):
    frame_path = frame_files[idx]
    new_path = os.path.join(frames_to_analyze_path, f"frame_{i}.jpg")
    os.replace(frame_path, new_path)  # Overwrite existing files if they exist

# Get the paths of the frames to analyze
frames_to_analyze = [os.path.join(frames_to_analyze_path, f) for f in os.listdir(frames_to_analyze_path)]

# Perform object detection and tracking
direction = motion_recognition.detect_and_track_object(frames_to_analyze)

print("Object direction:", direction)
