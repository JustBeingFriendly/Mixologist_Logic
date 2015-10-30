#!/usr/bin/env python

'''
Hey this is an overlong example of how the queues and lists will return values
This is ment to be run from the command line but can be easily cut and paste into bottle to get a return
If your having trouble let me know :D
'''

from collections import deque
from collections import namedtuple


#class QueueControl:
def createDeque():
    aList = [] #This will be returned at the end
    d = deque([],10) #Creates an empty deque [pronounced deck]
    order = namedtuple('DrinkOrder', ['UserID', 'Drink', 'OrderNumber']) #Creates a namedtuple

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
    bList = createDeque()
    print '\nTuple in position 0 in bList: '
    print bList[0][0]
    print bList[0][1]
    print bList[0][2]
    print bList[0]
    print '\nTuple 3 in position 3 in bList in reverse order: '
    print bList[3][2]
    print bList[3][1]
    print bList[3][0]
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
print tup[1:]
print tup1[0:]

'''

