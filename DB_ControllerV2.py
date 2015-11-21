#!/usr/bin/env python

import sqlite3
import sys
import os
from CreateDrinktionaryDB import createDB

dbName = 'drinktionary.db'

#Query database with name of drink, sets how many revolutions the flowmeter will do
def getDatabaseOutput(drinkRequest):
    
    drinkName = ""
    Rum = 0
    Vodka = 0
    Coke = 0

    #Check if database exists
    if not os.path.exists(dbName):
        DBCreator = createDB
    
    #create connection string
    conn = sqlite3.connect(dbName)
    #create cursor for enumeration
    c = conn.cursor()
    #Create query string
    try:
        c.execute('SELECT name, Rum, Vodka, Coke FROM drinks where name LIKE?', (drinkRequest,))
        drinkName, Rum, Vodka, Coke = c.fetchone()
    except:
        sys.exit("Bad input, please check the string you're passing to Queue_Controller.py (getDatabaseOutput())\n\r")
    #Check database return
    if drinkName == "":
        sys.exit("Error retrieving database info (getDatabaseOutput())")
    #Close connection
    conn.close()
    aTup = (Rum, Vodka, Coke)
    return aTup


def get_drinks_List():
    if not os.path.exists(dbName):
        DBCreator = createDB
        
    conn = sqlite3.connect(dbName)
    c = conn.cursor()    
    c.execute('SELECT name FROM drinks')
    drinkList = []    
    for row in c:
        drinkList.append(row[0])        
    conn.close()
    return drinkList
