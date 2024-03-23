import requests

def download_file(url, filename):
    # Stream download to handle large files
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

# URLs for the YOLOv3 weights and cfg
yolo_urls = {
    "yolov3.weights": "https://pjreddie.com/media/files/yolov3.weights",
    "yolov3.cfg": "https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg?raw=true",
}

# Download each file
for filename, url in yolo_urls.items():
    print(f"Downloading {filename}...")
    download_file(url, filename)
    print(f"Finished downloading {filename}.")
