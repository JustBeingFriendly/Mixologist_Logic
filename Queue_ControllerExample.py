#!/usr/bin/env python

'''
Hey this is an overlong example of how the queues and lists will return values
This is ment to be run from the command line but can be easily cut and paste
into bottle to get a return
If your having trouble let me know :D
'''

from collections import deque
from collections import namedtuple
global theQueue
theQueue = deque()

def createDeque():
    global theQueue
    aList = [] #This will be returned at the end
   
    order = namedtuple('DrinkOrder', ['UserID', 'Drink', 'OrderNumber']) #Creates a namedtuple

    nt = order('Mr_Android', 'Coke', 123)#Add values to the value fields of the named tuple
    theQueue.append(nt) #Append the named tupple to the deque
    nt = order('Mr_Web', 'Vodka', 124)
    theQueue.append(nt)
    nt= order('Mr_Android', 'Rum', 125)
    theQueue.append(nt)
    nt = order('Mr_Web', 'Rum and Coke', 126)
    theQueue.append(nt)
    nt = order('Mr_Web', 'Rum Neat', 127)
    theQueue.append(nt)
    nt = order('Mr_Web', 'Vodka Neat', 128)
    theQueue.append(nt)

    for order in theQueue:
        tup = (order.Drink, order.UserID, order.OrderNumber)
        aList.append(tup)
    return aList

def clientQueue(UserID):
    global theQueue
    aList = []
    for element in theQueue:
        if element[1] == UserID:
            aList.append(element)        
    return aList

def removeOrderFromQueue(OrderID):
    global theQueue
    tempQueue = deque()
    for item in theQueue:
        if item[2] != OrderID:
            tempQueue.append(item)
    theQueue.clear()
    theQueue = tempQueue

createDeque()
