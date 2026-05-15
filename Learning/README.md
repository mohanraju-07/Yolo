```markdown
# Folder Overview

The `Learning` folder contains two Python scripts, `yoloWIthVideo.py` and `yoloWithWebCam.py`, which utilize the You Only Look Once (YOLO) object detection algorithm for video analysis and webcam video feed processing.

## Scripts Overview

1.  `yoloWIthVideo.py`: This script reads a video file using OpenCV, applies the YOLOv8n object detection model to detect objects within the video frames, and tracks the detected objects across frames using the Sort algorithm. The script then displays the video feed with bounding boxes around the detected objects and counts the number of objects passing through a virtual gate.
2.  `yoloWithWebCam.py`: This script captures video feed from the default webcam using OpenCV, applies the YOLOv8n object detection model to detect objects within the video frames, and displays the video feed with bounding boxes around the detected objects, along with their confidence levels.

## File-by-File Explanation

### yoloWIthVideo.py

*   **Importing Libraries**: The script starts by importing the necessary libraries, including `ultralytics` for YOLO object detection, `cv2` (OpenCV) for video processing, `cvzone` for text and rectangle drawing on images, and `math` for mathematical operations.
*   **Loading Video and Model**: The script loads a video file using `cv2.VideoCapture` and initializes the YOLOv8n object detection model using `YOLO('yolov8n.pt')`.
*   **Setting Tracker and Limits**: The script sets up a tracker using the Sort algorithm and defines virtual gate limits to count objects passing through.
*   **Object Detection and Tracking**: Inside the `while` loop, the script reads frames from the video file, applies the YOLO object detection model to detect objects in each frame, and updates the tracker with the detected objects.
*   **Displaying Results**: The script draws bounding boxes around the detected objects, their confidence levels, and counts the number of objects passing through the virtual gate.

### yoloWithWebCam.py

*   **Importing Libraries**: The script starts by importing the necessary libraries, including `ultralytics` for YOLO object detection, `cv2` (OpenCV) for video processing, and `cvzone` for text and rectangle drawing on images.
*   **Loading Webcam and Model**: The script initializes the webcam using `cv2.VideoCapture(0)` and loads the YOLOv8n object detection model using `YOLO('../yolo-weights/yolov8n.pt')`.
*   **Object Detection**: Inside the `while` loop, the script reads frames from the webcam, applies the YOLO object detection model to detect objects in each frame, and draws bounding boxes around the detected objects with their confidence levels.

## Functions/Classes Explained

### sort.SORT (Object Tracker)

The Sort algorithm is used to track objects across frames. It uses a simple yet effective approach to associate the detections of different frames.

### yolo.YOLO (Object Detection Model)

The YOLOv8n object detection model is used to detect objects in video frames. It provides a high-accuracy and real-time object detection solution.

## Dependencies Used

### Libraries

*   `ultralytics`: For YOLO object detection
*   `cv2`: For video processing and image manipulation
*   `cvzone`: For text and rectangle drawing on images
*   `math`: For mathematical operations
*   `numpy`: For numerical computing (used indirectly through `np.empty` and `np.vstack`)

### Files

*   `yolov8n.pt`: The YOLOv8n object detection model file

## Installation

To run the scripts, make sure you have the necessary dependencies installed, including:

*   `ultralytics`: Install using pip: `pip install ultralytics`
*   `cv2`: Install using pip: `pip install opencv-python`
*   `cvzone`: Install using pip: `pip install cvzone`
*   `numpy`: Install using pip: `pip install numpy`

Also, ensure you have the YOLOv8n object detection model file `yolov8n.pt` in the `../yolo-weights` directory.
```