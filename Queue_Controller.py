#!/usr/bin/env python

import sqlite3
import sys
import os


#Initialise variables
dbName = 'drinktionary.db'
drinkName = ""
fluidQuantity1 = 0
fluidQuantity2 = 0
fluidQuantity3 = 0

#Check if database exists
if not os.path.exists(dbName):
    GPIO.cleanup()
    sys.exit("ERROR: %s doesn't exist in current directory \n\rexiting..." % (dbName))


#Function definitions


#Query database with name of drink, sets how many revolutions the flowmeter will do
def getDatabaseOutput():
    global drinkName
    global fluidQuantity1   
    #create connection string
    conn = sqlite3.connect(dbName)
    #create cursor for enumeration
    c = conn.cursor()
    #Create query string
    try:
        c.execute('SELECT name, fluidQuantity1 FROM drinks where name LIKE?', (userInput,))
        drinkName, fluidQuantity1, fluidQuantity2, fluidQuantity3 = c.fetchone()
    except:
        sys.exit("Bad input, please check the string you're passing to mixologist.py (getDatabaseOutput())\n\r")        
    #Check database return
    if drinkName == "":
        sys.exit("Error retrieving database info (getDatabaseOutput())")
    #Print to console name of drink    
    sys.stdout.write('Pouring %s \n\r' % drinkName)
    sys.stdout.flush()
    #Close connection
    conn.close()


