import numpy as np
import time
import imutils
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

avg = None

with PiCamera(resolution=(640,480), framerate=30) as camera:
    with PiRGBArray(camera, size=(640,480)) as rawCapture:
        for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            frame = f.array
            text = "Unoccupied"

            frame = imutils.resize(frame, width=500)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            
            if avg is None:
		print "[INFO] starting background model..."
		avg = gray.copy().astype("float")
		rawCapture.truncate(0)
		continue

            cv2.accumulateWeighted(gray, avg, 0.5)
            frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

            thresh = cv2.threshold(frameDelta, 5, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < 5000:
			continue
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"
            
            cv2.imshow("ab",frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            rawCapture.truncate(0)
