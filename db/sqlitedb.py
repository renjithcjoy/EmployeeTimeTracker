import sqlite3
from sqlite3 import Error
from datetime import datetime
import zlib

db_file = "data.db"
conn = None

# Windows table
WINDOWSTABLE = """CREATE TABLE IF NOT EXISTS windows (
	id integer PRIMARY KEY,
	windowname text NOT NULL,
    windowtitle text,
    usedtime INTEGER,
	date text,
	time text,
    datetime text
);"""

def create_connection():
    """ create a database connection to a SQLite database """
    global conn
    if conn != None: 
        return conn
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn



def create_table():
    global conn
    retvalue = False
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute(WINDOWSTABLE)
        retvalue = True
    except Error as e:
        print(e)
    return retvalue


def insert_data(windowname,windowtitle,usedtime):
    global conn

    retvalue = False

    now = datetime.now()
    date_string = now.strftime("%d-%m-%Y")
    time_string = now.strftime("%H:%M:%S")
    datetime_string = date_string+" "+time_string
    sql = ''' INSERT INTO windows(windowname,windowtitle,usedtime,date,time,datetime)
              VALUES(?,?,?,?,?,?) '''

    try:
        conn = create_connection()
        cur = conn.cursor()
        data_tuple = (windowname,windowtitle,usedtime,date_string,time_string,datetime_string)
        cur.execute(sql, data_tuple)
        conn.commit()
        retvalue = True
    except Error as e:
        print("insert_data ",e)

    return retvalue
    
    


def select_all_data():
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM windows")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

    

    

    

