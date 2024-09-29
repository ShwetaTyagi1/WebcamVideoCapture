# WebcamVideoCapture

## Overview:
This project captures video directly from the webcam, resizes it, and saves it in `.avi` format. The videos are stored with a unique filename, preventing accidental overwriting of previously recorded videos. The script allows easy video processing options like resizing, flipping frames, and converting frames to grayscale.

## Features:
- Captures video using the webcam.
- Automatically generates unique filenames for saved videos.
- Resizes video frames to a fixed resolution (550x550 pixels).
- Allows flipping of frames or converting to grayscale (commented for easy customization).
- Saves videos in `.avi` format using XVID encoding.
- Simple, well-commented code to modify and expand further.

## Technologies Used:
- **Python**: The core programming language.
- **OpenCV**: For capturing and processing video frames.
- **OS**: To manage file paths and generate unique filenames.

## How to Use:

### Requirements:
- Python 3.x
- Required Python libraries:
    - `opencv-python`

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Webcam-Video-Capture.git
   cd Webcam-Video-Capture
   ```
2. Install the required dependency:
   ```bash
   pip install opencv-python
   ```

### Usage:
1. **Run the script**:
   ```bash
   python webcam_capture.py
   ```

2. **Controls**:
   - The video will display on your screen.
   - **Press 'q'** to stop recording and save the video.

3. **Customization**:
   - Change the resolution of the video frames by editing the `cv2.resize(frame, (550,550))` line.
   - To **flip** the video, uncomment the line:  
     ```python
     frame = cv2.flip(frame, 0)
     ```
   - To convert the video to **grayscale**, modify the script as follows:
     - Add a `gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)` line after capturing the frame.
     - Replace `frame` with `gray` in the `output.write()` function.

## Example Output: 
Captured videos will be saved in the `C:/Users/Shweta Tyagi/Computer Vision Project outputs/` folder with unique filenames like `output_1.avi`, `output_2.avi`, etc.
Make modifications according to your system for proper save functionality.

---

## Contributing:
Feel free to contribute by submitting pull requests, suggesting new features, or reporting issues.



