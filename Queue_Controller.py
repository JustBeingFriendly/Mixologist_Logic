#!/usr/bin/env python

from collections import deque
from collections import namedtuple

theQueue = deque()
OrderNumber = 0
order = namedtuple('DrinkOrder', ['UserID', 'Drink', 'OrderNumber'])

def addAndroidToQueue(inTuple):    
    global order
    global OrderNumber
    global theQueue
    OrderNumber += 1
    aTuple = order(inTuple[0], inTuple[1], OrderNumber)    
    theQueue.append(aTuple)
    timeTillPour = len(theQueue) * 30
    orderNumAndTime = (OrderNumber, timeTillPour)
    return orderNumAndTime
    
def addWebToQueue(inTuple):
    global OrderNumber
    global theQueue
    OrderNumber += 1
    aTuple = order(inTuple[0], inTuple[1], OrderNumber)#0 = UserID, 1 = DrinkName    
    theQueue.append(aTuple)

def removeOrderFromQueue(OrderID):
    global theQueue
    tempQueue = deque()
    for item in theQueue:
        if item[2] != int(OrderID):
            tempQueue.append(item)
    theQueue.clear()
    theQueue = tempQueue
    tempQueue = deque()
        
def userOrderQueue(UserID):
    global theQueue
    aList = []    
    for item in theQueue:        
        if (item[0] == UserID):
            tup = (item[1],item[2])
            aList.append(tup)
    return aList

def firstInQueue(UserID):
    global theQueue
    if theQueue:
        aTup = theQueue[0]
        if aTup[0] == UserID:
            return aTup
    else:
        aTup = ("Not Yet", "Not Yet","Not Yet")
        return aTup
    
'''
def test():
    tup = ("Mr_Android", "Rum & Coke")
    addAndroidToQueue(tup)
    tup = ("Mr_Android", "Coke")
    addAndroidToQueue(tup)
    tup = ("Mr_Android", "Vodka & Coke")
    addAndroidToQueue(tup)
    firstInQueue()
  
    global theQueue
    for item in theQueue:
        print item
    removeOrderFromQueue(3)
    for item in theQueue:
        print item
       
test()


jList = userOrderQueue("Mr_Android")
print "queue test"
for item in jList:
    print item
'''
