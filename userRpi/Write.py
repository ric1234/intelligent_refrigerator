#!/usr/bin/env python3

import RPi.GPIO as GPIO
import SimpleMFRC522
reader = SimpleMFRC522.SimpleMFRC522()

try:
        text = raw_input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()
