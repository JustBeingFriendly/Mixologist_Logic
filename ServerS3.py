#!/usr/bin/env python

from bottle import route, run, post, put, request
import json
import sqlite3
from Queue_Controller import addAndroidToQueue, userOrderQueue

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

#Receives a json object, process it, then returns it to sender
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
    for item in aList:
        print item[0]
        
    jsonObject = []
    for item in aList:
        data = {"Drink" : item[0], "OrderID" : item[1]}
        jsonObject.append(data)
    
    for item in jsonObject:
         print item

    #print jsonObject 
    #return json.dumps(aList)
    return json.dumps(jsonObject)
    
run (host='192.168.0.107', port=8081, debug=True)


