import cv2
import os
import stocking_recognition

def extract_specific_frames(video_path, output_path, percentages=[30, 70]):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    video_length_seconds = total_frames / frame_rate

    # Calculate frame numbers for the specified percentages
    frame_numbers = [int(total_frames * (p / 100)) for p in percentages]
    
    for i, frame_number in enumerate(frame_numbers):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()
        if ret:
            output_file = os.path.join(output_path, f"frame_at_{percentages[i]}_percent.jpg")
            cv2.imwrite(output_file, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        else:
            print(f"Error: Could not read frame at {percentages[i]}%")

    cap.release()

def video_analysis(video_path):
    output_path = "output_frames"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    extract_specific_frames(video_path, output_path)

    # Get the paths of the frames to analyze
    frames_to_analyze = ["output_frames/frame_at_30_percent.jpg", "output_frames/frame_at_70_percent.jpg"]

    return stocking_recognition.process_images_and_detect_motion(frames_to_analyze)
    

print(video_analysis("final_test_files/stocking_videos/potato_in.mp4"))  # Example usage