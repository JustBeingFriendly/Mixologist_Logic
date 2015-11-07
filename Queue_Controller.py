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

    #if(OrderNumber%5 == 0 ):
    #    theQueue.popleft()
    
    aTuple = order(inTuple[0], inTuple[1], OrderNumber)    
    theQueue.append(aTuple)    
    #print theQueue[-1]
    timeTillPour = len(theQueue) * 30
    orderNumAndTime = (OrderNumber, timeTillPour)
    #userOrderQueue(inTuple[0])
    return orderNumAndTime
    
def addWebToQueue(inTuple):
    global OrderNumber
    global theQueue
    OrderNumber += 1
    aTuple = order(inTuple[0], inTuple[1], OrderNumber)#0 = UserID, 1 = DrinkName    
    theQueue.append(aTuple)

def userOrderQueue(UserID):
    global theQueue
    aList = []    
    for item in theQueue:
        if (item[0] == UserID):
            tup = (item[1],item[2])
            aList.append(tup)
    #print theQueue
    #print aList
    return aList           

'''
def UserOrderQueueTester(UserID):
    aList = userOrderQueue(UserID)

    for item in aList:
        print item[1], item[0]        
        
    return aList

def androidSimulator():
    global order
    tempTup = ('Mr_Android', 'Rum and Coke')
    j = 5
    i = 0
    while i < j:
        #addAndroidToQueue(tempTup)
        i += 1
        
    UserOrderQueueTester('Mr_Android')        
'''
#androidSimulator()



