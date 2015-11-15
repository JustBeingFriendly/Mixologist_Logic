#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

bTime = 170

isA = False
isB = False
isC = False

#Initialise GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT) #Solenoid_1
GPIO.setup(19,GPIO.OUT) #Solenoid_2
GPIO.setup(26,GPIO.OUT) #Solenoid_3

GPIO.setup(17, GPIO.IN) #Flowmeter_1
GPIO.setup(27, GPIO.IN) #Flowmeter_2
GPIO.setup(22, GPIO.IN) #Flowmeter_3

rotationsA = 0
rotationsB = 0
rotationsC = 0

def liquidflow_A_Callback(channel):
    global rotationsA
    rotationsA += 1
    if isA:
        print "Rum: " + str(rotationsA)

def liquidflow_B_Callback(channel):
    global rotationsB
    rotationsB += 1
    if isB:
        print "Vodka: " + str(rotationsB)    

def liquidflow_C_Callback(channel):
    global rotationsC
    rotationsC += 1
    if isC:
        print "Coke: " + str(rotationsC)

GPIO.add_event_detect(17, GPIO.FALLING, callback=liquidflow_A_Callback, bouncetime=bTime)
GPIO.add_event_detect(27, GPIO.FALLING, callback=liquidflow_B_Callback, bouncetime=(bTime + 50))
GPIO.add_event_detect(22, GPIO.FALLING, callback=liquidflow_C_Callback, bouncetime=bTime)

def firstLine(numToRotate):
    global isA
    isA = True
    global rotationsA
    rotationsA = 0
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)        
    while rotationsA < numToRotate:
        dumbNum = 1            
    GPIO.output(13, GPIO.HIGH)
    isA = False

def secondLine(numToRotate):
    global isB
    isB = True
    global rotationsB
    rotationsB = 0
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)            
    while rotationsB < numToRotate:
        dumbNum = 1
    GPIO.output(19, GPIO.HIGH)
    isB = False     

def thirdLine(numToRotate):
    global isC
    isC = True
    global rotationsC
    rotationsC = 0
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)                
    while rotationsC < numToRotate:
        dumbNum = 1
    GPIO.output(26, GPIO.HIGH)          
    isC = False
    
def processGPIO(rumNum, vodkaNum, cokeNum):
    try:
        if rumNum != 0:
            firstLine(rumNum)
        if vodkaNum != 0:
            secondLine(vodkaNum)
        if cokeNum != 0:
            thirdLine(cokeNum)        
        
    except KeyboardInterrupt:    
        GPIO.cleanup()
        
def makeDrink(inTup):
    rumNum = int(inTup[0])
    vodkaNum = int(inTup[1])
    cokeNum = int(inTup[2])
    processGPIO(rumNum, vodkaNum, cokeNum)
    GPIO.cleanup()


