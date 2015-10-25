#!/usr/bin/env python

import sqlite3
import os

databaseIsNew = not os.path.exists('drinktionary.db')


if databaseIsNew:
    print 'Creating new database drinktionary.db'
    
    #create connection string
    conn = sqlite3.connect('drinktionary.db')

    #create cursor for enumeration
    c = conn.cursor()

    #create table
    c.execute('''CREATE TABLE drinks
                    (id INTEGER PRIMARYKEY, name TEXT, fluidQuantity1 INTEGER,
                     fluidQuantity2 INTEGER, fluidQuantity3 INTEGER)''')

    #insert a row of data
    c.execute("INSERT INTO drinks VALUES(1 ,'Water', 6, 0, 0)")
    c.execute("INSERT INTO drinks VALUES(2 ,'Pepsi', 10, 0, 0)")

    #Save (commit) the changes
    conn.commit()

    print 'drinktionary.db created in current directory'
    
    #close the connection
    conn.close()
    
else:
    print 'drinktionary.db already exists in current directory ...exiting'
