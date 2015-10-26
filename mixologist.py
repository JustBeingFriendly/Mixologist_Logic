#!/usr/bin/env python

import RPi.GPIO as GPIO
import sqlite3
import sys
import os
from time import sleep

#Initialise GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT) #Solenoid
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Liquid Flowmeter

#Initialise variables
dbName = 'drinktionary.db'
rotations = 0
mlCount = 0
drinkName = ""
fluidQuantity1 = 0
fluidQuantity2 = 0
fluidQuantity3 = 0

#Check if database exists
if not os.path.exists(dbName):
    GPIO.cleanup()
    sys.exit("ERROR: %s doesn't exist in current directory \n\rexiting..." % (dbName))

#function for event listener to callback to
def liquidflowMeasurement(channel):
    global rotations
    global mlCount
    rotations += 1
    mlCount = rotations * 4
    sys.stdout.write('ml dispensed: ' + str(mlCount) + '\r')
    sys.stdout.flush()

#Add event listener to listen for flowmeter signal
GPIO.add_event_detect(21, GPIO.FALLING, callback=liquidflowMeasurement)

#Function definitions

#Checks if any parameters were passed when this was called, if not exit
def getInputArguments():    
    if len(sys.argv) == 1:
        GPIO.cleanup()
        sys.exit("ERROR: no arguments supplied to mixologist.py (getInputArguments())")   
    return str(sys.argv[1])

#Query database with name of drink, sets how many revolutions the flowmeter will do
def getDatabaseOutput():
    global drinkName
    global fluidQuantity1
    #If the next statement fails the program exits
    userInput = getInputArguments()    
    #create connection string
    conn = sqlite3.connect(dbName)
    #create cursor for enumeration
    c = conn.cursor()
    #Create query string
    try:
        c.execute('SELECT name, fluidQuantity1 FROM drinks where name LIKE?', (userInput,))
        drinkName, fluidQuantity1 = c.fetchone()
    except:
        GPIO.cleanup()        
        sys.exit("Bad input, please check the string you're passing to mixologist.py (getDatabaseOutput())\n\r")        
    #Check database return
    if drinkName == "":
        GPIO.cleanup()
        sys.exit("Error retrieving database info (getDatabaseOutput())")
    #Print to console name of drink    
    sys.stdout.write('Pouring %s \n\r' % drinkName)
    sys.stdout.flush()
    #Close connection
    conn.close()
    
''' Controls the gpio pins on the rPi. Opens the solenoid, once the number of flowmeter revolutions completes
The solenoid closes '''
def processGPIO():
    try:    
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)

        while rotations < fluidQuantity1:
            dumbNum = 1
            
        GPIO.output(18, GPIO.HIGH)
        sys.stdout.write('\n\r')
        sys.stdout.flush()
        sys.stdout.write('Enjoy your %s \n\r' % (drinkName))
        sys.stdout.flush()
    except KeyboardInterrupt:    
        GPIO.cleanup()
        sys.stdout.write('\n\r')
        sys.stdout.flush()

getDatabaseOutput()
processGPIO()
 
GPIO.cleanup()

