#!/usr/bin/env python

from collections import deque
from collections import namedtuple

theQueue = deque()
HighestOrderNumber = 0
order = namedtuple('DrinkOrder', ['UserID', 'Drink', 'OrderNumber'])

def addAndroidToQueue(inTuple):    
    global order
    global HighestOrderNumber
    global theQueue
    HighestOrderNumber += 1
    aTuple = order(inTuple[0], inTuple[1], HighestOrderNumber)    
    theQueue.append(aTuple)    
    print theQueue[-1]
    
def addWebToQueue():
    global HighestOrderNumber
    global theQueue
    HighestOrderNumber += 1

def androidSimulator():
    global order
    tempTup = ('Mr_Android', 'Rum and Coke')
    j = 5
    i = 0
    while i < j:
        addAndroidToQueue(tempTup)
        i += 1    

#androidSimulator()

'''
def createDeque():
    global order
    aList = [] #This will be returned at the end
    d = deque([],10) #Creates an empty deque [pronounced deck]
    nt = order('Mr_Android', 'Coke', 123)#Add values to the value fields of the named tuple
    d.append(nt) #Append the named tupple to the deque
    nt = order('Mr_Web', 'Vodka', 124)
    d.append(nt)
    nt= order('Mr_Android', 'Rum', 125)
    d.append(nt)
    nt = order('Mr_Web', 'Rum and Coke', 126)
    d.append(nt)

    for order in d:
        tup = (order.Drink, order.UserID, order.OrderNumber)
        aList.append(tup)
    return aList


def tupInterpret():
    global order
    bList = createDeque()
    tup = (bList[0][0], bList[0][1])
    addAndroidToQueue(tup)
    
    
    print '\nTuple in position 0 in bList: '
    print [0]
    print bList[0][1]
    print bList[0][2]
    print bList[0]
    print '\nTuple 3 in position 3 in bList out of order: '
    print bList[3][1]
    print bList[3][0]
    print bList[3][2]
    print bList[3]
    print '\nAll elements for Mr_Web in bList: '    
    for tp in bList:
        if tp[1] == 'Mr_Web':
            print tp
    print '\nAll elements for Mr_Android in bList: '
    for tp in bList:
        if tp[1] == 'Mr_Android':
            print tp
   
    
    
tupInterpret()
'''


