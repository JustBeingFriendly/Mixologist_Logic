#!/usr/bin/env python
'''

'''
import RPi.GPIO as GPIO
from time import sleep

#Initialise GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT) #Solenoid1
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Flowmeter1

#Initialise variables
rotations = 0
fluidQuantity1 = 0 #Flowmeter (GPIO:21), Solenoid (GPIO:18)
fluidQuantity2 = 0
fluidQuantity3 = 0

#function for event listener to callback to
def liquidflowCallback(channel):
    global rotations
    rotations += 1
    
#Add event listener to listen for flowmeter signal
GPIO.add_event_detect(21, GPIO.FALLING, callback=liquidflowCallback)

    
''' Controls the gpio pins on the rPi. Opens the solenoid,
once the number of flowmeter rotations completes the solenoid closes '''
def processGPIO():
    try:
        #Flowmeter (GPIO:21), Solenoid (GPIO:18)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)

        while rotations < fluidQuantity1:
            dumbNum = 1
            
        GPIO.output(18, GPIO.HIGH)
        
    except KeyboardInterrupt:    
        GPIO.cleanup()

GPIO.cleanup()

