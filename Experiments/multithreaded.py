#!/usr/bin/python3

import threading
import time

import no_args as ic

tensorLock = threading.Lock()
exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name)
      print ("Exiting " + self.name)

def print_time(threadName):
   if exitFlag:
      threadName.exit()
   tensorLock.acquire()
   print("Success1")
   ic.main('Cropped01.jpg')
   tensorLock.release()

class NotmyThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_timer(self.name)
      print ("Exiting " + self.name)

def print_timer(threadName):
   if exitFlag:
      threadName.exit()
   tensorLock.acquire()
   print("Success2")
   ic.main('Cropped11.jpg')
   tensorLock.release()
# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = NotmyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")