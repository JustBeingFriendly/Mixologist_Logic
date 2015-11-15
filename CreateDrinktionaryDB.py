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
                        Rum INTEGER,
                        Vodka INTEGER,
                        Coke INTEGER
                        )''')

        #insert a row of data
        c.execute("INSERT INTO drinks VALUES( 1,'Rum Neat'        ,18, 0, 0)")
        c.execute("INSERT INTO drinks VALUES( 2,'Vodka Neat'      , 0,18, 0)")
        c.execute("INSERT INTO drinks VALUES( 3,'Rum & Coke'      ,18, 0,39)")
        c.execute("INSERT INTO drinks VALUES( 4,'Vodka & Coke'    , 0,18,39)")
        c.execute("INSERT INTO drinks VALUES( 5,'Coke'            , 0, 0,39)")

        #Save (commit) the changes
        conn.commit()

        print 'drinktionary.db created in current directory'
        
        #close the connection
        conn.close()
        
    else:
        print 'drinktionary.db already exists in current directory ...exiting'

createDB()
