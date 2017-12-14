#!/usr/bin/env python3

import RPi.GPIO as GPIO
import SimpleMFRC522
import second as sc
import firstwin as fi

reader = SimpleMFRC522.SimpleMFRC522()
def rfid(): 
    try:
        flag=0
        print("Place the tag")
        id, text = reader.read()
        print(id)
        #check id on card
        if id == 137721249437:
            print ("Authenticated")
            flag=1
            #sc.voiceui()
            #ch.choice()
        else:
           fi.fail() 
            
    finally:
        #clean GPIO stup
        GPIO.cleanup()
    return flag
