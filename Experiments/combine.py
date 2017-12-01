
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sys
#OpenCV libraries
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
 
print("Full image captured")
'''

'''
#Segmenting an image
#Divide the image into 4 equal parts
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

'''
#include Tensor flow library file
sys.path.append('/home/pi/Desktop/Experiments/')
import no_args as ic

#ic.main('Cropped00.jpg')
itemDetected=ic.main('Cropped01.jpg')
#print("I found a %s" %(itemDetected))

#ic.main('Cropped10.jpg')
#ic.main('Cropped11.jpg')
'''
##############################################
#Use multithreading approach to obtain the image

import threading
import time

import no_args as ic

#Lock to ensure synchronization
tensorLock = threading.Lock()
exitFlag = 0

import data_present as dat
foodItems = []

class myThread (threading.Thread):
   def __init__(self, threadID, name, image_file):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.image_file = image_file
   def run(self):
      print ("Starting " + self.name)
      run_tensoflow(self.name, self.image_file)
      print ("Exiting " + self.name)

def run_tensoflow(threadName,image_file):
   if exitFlag:
      threadName.exit()
   tensorLock.acquire()
   print("Lock acq by " + str(threadName))
   itemDetected=ic.main(image_file)
   foodItems.append(itemDetected)
   tensorLock.release()


threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
image_filesList= ["Cropped00.jpg", "Cropped01.jpg", "Cropped10.jpg", "Cropped11.jpg"]
threads = []
threadID = 0
imList = 0

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, image_filesList[imList])   
   thread.start()
   threads.append(thread)   #Appends the thread to the list of threads
   threadID += 1
   imList += 1


# Wait for all threads to complete
for t in threads:
   t.join()
   
dat.addToDictionary(foodItems)
print ("Exiting Main Thread")

#################################################



#How to use the datastructure
'''
import data_present as dat
foodItems = []
foodItems.append(itemDetected)
dat.addToDictionary(foodItems)
'''

'''
cv2.waitKey(27)
cv2.destroyAllWindows()
'''
#############################################################