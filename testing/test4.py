import sqlite3
from sqlite3 import Error
from datetime import datetime

db_file = "data.db"

# Windows table
WINDOWSTABLE = """CREATE TABLE IF NOT EXISTS windows (
	id integer PRIMARY KEY,
	windowname text NOT NULL,
    windowtitle text,
	date text,
	time text,
    datetime text
);"""

conn = None

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



def create_table(conn, create_table_sql):
    retvalue = False
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        retvalue = True
    except Error as e:
        print(e)
    return retvalue


def insert_data(conn, windowname,windowtitle):
    now = datetime.now()
    date_string = now.strftime("%d-%m-%Y")
    time_string = now.strftime("%H:%M:%S")
    datetime_string = date_string+" "+time_string
    sql = ''' INSERT INTO windows(windowname,windowtitle,date,time,datetime)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, windowname,windowtitle,date_string,time_string,datetime_string)
    conn.commit()


def select_all_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows")

    rows = cur.fetchall()

    for row in rows:
        print(row)

