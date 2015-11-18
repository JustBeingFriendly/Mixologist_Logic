#!/usr/bin/env python

from bottle import route, run, post, put, request
import json
import sqlite3
import RPi.GPIO as GPIO
from Queue_Controller import addAndroidToQueue, userOrderQueue, removeOrderFromQueue, firstInQueue, beginDrinkPouring

#This uiytrjyutd a json return
@route('/drinksList', method='GET')
def drink_send():
    drinkList = []
    drinkList = get_drinks_List()    
    jsonObject = []
    for item in drinkList:
        data = {"DrinkName" : item}
        jsonObject.append(data)
    return json.dumps(jsonObject)

#Retrieves available drinks list from drinktionary
def get_drinks_List():
    conn = sqlite3.connect('drinktionary.db')
    c = conn.cursor()    
    c.execute('SELECT name FROM drinks')
    drinkList = []    
    for row in c:
        drinkList.append(row[0])        
    conn.close()
    return drinkList

#Receives a json object, process it, then return ordernumber and time till ready
@route('/chooseDrink', method='PUT')
def choose_drink():
    id = request.json['UserID']
    drink = request.json['Drink']
    tup = (id, drink)    
    orderNumAndTime = addAndroidToQueue(tup)
    return json.dumps({"OrderNumber" : orderNumAndTime[0], "Time" : orderNumAndTime[1]})

@route('/getQueue', method='PUT')
def get_Queue():
    UserID = request.json['UserID']
    aList = userOrderQueue(UserID)    
    jsonObject = []
    for item in aList:
        data = {"Drink" : item[0], "OrderID" : item[1]}
        jsonObject.append(data)
    return json.dumps(jsonObject)

@route('/cancelOrder', method='PUT')
def cancel_Order():
    OrderID = request.json['OrderID']
    removeOrderFromQueue(OrderID)
    
@route('/firstInQueue', method='PUT')
def getFirstInQueue():
    UserID = request.json['UserID']
    aTup = firstInQueue(UserID)   
    return json.dumps({"UserID" : aTup[0], "Drink" : aTup[1],"OrderID" : aTup[2]})

@route('/pourDrink', method='PUT')
def pourTheDrink():
    OrderID = request.json['OrderID']
    aString = beginDrinkPouring(OrderID)
    return ({"ServerSays" : aString})
    #aTup = firstInQueue(UserID)   
    #return json.dumps({"UserID" : aTup[0], "Drink" : aTup[1],"OrderID" : aTup[2]})

run (host='192.168.0.107', port=8081, debug=True)
'''
try:
    GPIO.cleanup()
    run (host='192.168.0.107', port=8081, debug=True)

except KeyboardInterrupt:    
    GPIO.cleanup()
'''

