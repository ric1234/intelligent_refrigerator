# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import numpy as np
import argparse

import cv2

from matplotlib import pyplot as plt


 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(0.1)
 
# grab an image from the camera
camera.resolution=(1024,768)     #This line if removed gives the full 1980x1080 resolution
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
 
print("Image captured") 
# display the image on screen and wait for a keypress
#cv2.imshow("Image", image)

###################################################

if image.shape[-1] == 3:           # color image
    print("Shape issue")
    b,g,r = cv2.split(image)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])     # switch it to rgb
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    print("No shape issue")
    gray_img = image

img = cv2.medianBlur(gray_img, 5)
print("Median blue")
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=80,param2=60,minRadius=0,maxRadius=0)
#Default threshods are param1=50 and param2=30
#can return error if no circle detected
#error checking needs to be done
print("Hough done")
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
print("Number of circles: " + str(len(circles[0])))

plt.subplot(121),plt.imshow(rgb_img)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cimg)
plt.title('Hough Transform'), plt.xticks([]), plt.yticks([])
plt.show()
