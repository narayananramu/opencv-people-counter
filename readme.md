# OpenCV People Counter
This program counts number of people incomming and outgoing a particular door. The example video is shot with Raspberry Pi Camera. I use OpenCV and Python 2.7. Make sure you install the `numpy`, `cv2`, `imutils` before you run the program.

Steps to execute the program with video source
1. Make sure you install the above mentioned dependencies.
2. Place your video file and replace `people-capture.mp4` in the line `video = cv2.VideoCapture("people-capture.mp4")` with your video filename
3. Open your Terminal in OpenCV Environment
4. Run `python counter.py`

Steps to execute the program on Raspyberry Pi 3
1. Make sure you install the above mentioned dependencies.
2. Also make sure you have camera connected to your Pi3.
3. Open your Terminal in OpenCV Environment
4. Run `python raspberry.py`

This is ain't a perfect solution for all use cases, I will be constantly improving algorithm. In the next update I am working to integrate the algorithm with custom haar cascade.
