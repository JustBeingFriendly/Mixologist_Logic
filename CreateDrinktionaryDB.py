#!/usr/bin/env python

import sqlite3
import os

def createDB():
    databaseIsNew = not os.path.exists('drinktionary.db')


    if databaseIsNew:
        print 'Creating new database drinktionary.db'
        
        #create connection string
        conn = sqlite3.connect('drinktionary.db')

        #create cursor for enumeration
        c = conn.cursor()

        #create table
        c.execute('''CREATE TABLE drinks (
                        id INTEGER PRIMARYKEY,
                        name TEXT,
                        fluidQuantity1 INTEGER,
                        fluidQuantity2 INTEGER,
                        fluidQuantity3 INTEGER
                        )''')

        #insert a row of data
        c.execute("INSERT INTO drinks VALUES( 1,' Coke'       ,39, 0, 0)")
        c.execute("INSERT INTO drinks VALUES( 2,'Rum & Coke'  ,26,13, 0)")
        c.execute("INSERT INTO drinks VALUES( 3,'Vodka & Coke',26, 0,13)")
        c.execute("INSERT INTO drinks VALUES( 4,'Rum Neat'    , 0,13, 0)")
        c.execute("INSERT INTO drinks VALUES( 5,'Vodka Neat'  , 0, 0,13)")

        #Save (commit) the changes
        conn.commit()

        print 'drinktionary.db created in current directory'
        
        #close the connection
        conn.close()
        
    else:
        print 'drinktionary.db already exists in current directory ...exiting'

createDB()
