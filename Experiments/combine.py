#Capture the image live
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

#Capture the image live
'''
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(0.1)
 
# grab an image from the camera
camera.resolution=(1024,1024)  #1024,768   #This line if removed gives the full 1980x1080 resolution
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

cv2.imwrite("full.jpg", image)
 
print("Image captured")
'''
'''
#Segmenting an image
image=cv2.imread("full.jpg")
roi_image_00 = image[0:511, 0:511]
roi_image_01 = image[0:511, 512:1023]
roi_image_10 = image[511:1023, 0:512]
roi_image_11 = image[511:1023, 511:1023]
cv2.imwrite("Cropped00.jpg",roi_image_00)
cv2.imwrite("Cropped01.jpg",roi_image_01)
cv2.imwrite("Cropped10.jpg",roi_image_10)
cv2.imwrite("Cropped11.jpg",roi_image_11)
'''


#This cakks the Tensor flow library

sys.path.append('/home/pi/Desktop/Experiments/')
import no_args as ic

#ic.main('Cropped00.jpg')
itemDetected=ic.main('Cropped01.jpg')
#print("I found a %s" %(itemDetected))

#ic.main('Cropped10.jpg')
#ic.main('Cropped11.jpg')


#How to use the datastructure

import data_present as dat
foodItems = []
foodItems.append(itemDetected)
dat.addToDictionary(foodItems)


'''
cv2.waitKey(27)
cv2.destroyAllWindows()
'''
#############################################################