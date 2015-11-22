#!/usr/bin/env python

from collections import deque
from collections import namedtuple
from DB_ControllerV2 import getDatabaseOutput
#import GPIO_processor  
from GPIO_processor import makeDrink

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
    print "\nPlace - Drink: " + str(aTuple[1]) + ", OrderID: " + str(aTuple[2]) + ", ClientID: " + str(aTuple[0])
    timeTillPour = len(theQueue) * 30
    orderNumAndTime = (OrderNumber, timeTillPour)
    return orderNumAndTime
    
def addWebToQueue(DrinkName):
    global OrderNumber
    global theQueue
    OrderNumber += 1
    aTuple = order('Mr_Web', DrinkName, OrderNumber)#0 = UserID, 1 = DrinkName    
    theQueue.append(aTuple)
    print "\nPlace - Drink: " + str(aTuple[1]) + ", OrderID: " + str(aTuple[2]) + ", ClientID: " + str(aTuple[0])

def removeOrderFromQueue(OrderID):
    global theQueue
    tempQueue = deque()
    for item in theQueue:
        if item[2] != int(OrderID):
            tempQueue.append(item)
        else:
            print "\nCancel  - Drink: " + str(item[1]) + ", OrderID: " + str(item[2]) + ", ClientID: " + str(item[0])
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
    else:
        aTup = ("Not Yet", "Not Yet","Not Yet")
        return aTup

def beginDrinkPouring(OrderID):
    global theQueue
    checkTup = theQueue.popleft()    
    if int(OrderID) == int(checkTup.OrderNumber):
        #print "OrderID == checkTup.OrderNumber"
        aTup = getDatabaseOutput(checkTup.Drink)
        print "\nPour  - Drink: " + str(checkTup[1]) + ", OrderID: " + str(checkTup[2]) + ", ClientID: " + str(checkTup[0])
        makeDrink(aTup)
        return "Success Pouring Drink"
    else:
        print "OrderID != checkTup.OrderNumber"
        return "You've had enough for one night"
'''
def test():
    tup = ("Mr_Android", "Rum & Coke")
    addAndroidToQueue(tup)
    tup = ("Mr_Android", "Coke")
    addAndroidToQueue(tup)
    tup = ("Mr_Android", "Vodka & Coke")
    addAndroidToQueue(tup)
    beginDrinkPouring("1")
           
test()


jList = userOrderQueue("Mr_Android")
print "queue test"
for item in jList:
    print item
'''
