#!/usr/bin/env python

from bottle import * #route, run, post, put, request
import json
import sqlite3

#This is intended as an example of a json return
@route('/', method='GET')
def drink_send():
    drinkList = []
    drinkList = list_drink()
    #return json.JSONEncoder(drinkList)
    return json.dumps(drinkList)

#Receives a json object, process it, then returns it to sender
@route('/chooseDrink', method='PUT')
def drink_send():
    id = request.json['id']
    drink = request.json['drink']
    bString = "Drink: " + drink + " \nID: " + id
    print bString
    return request.json

#Called from drink_send, this retrieves the drink list from the drinktionary
def list_drink():
    conn = sqlite3.connect('drinktionary.db')
    c = conn.cursor()    
    c.execute('SELECT name FROM drinks')
    drinkList = []
    
    for row in c:
        drinkList.append(row[0])
        
    conn.close()
    return drinkList
    
run (host='192.168.0.107', port=8081, debug=True)


