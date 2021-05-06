import sys
sys.path.insert(0, './db')
import sqlitedb
dbtype = "sqlite"


def create_connection():
    """ create a database connection to a SQLite database """
    global dbtype
    conn = None
    if dbtype == "sqlite":     
        try:
            conn = sqlitedb.create_connection()
        except Exception as e:
            print("Exception thrown while create_connection: {}".format(e))
    return conn



def create_table():
    
    global dbtype
    retvalue = False
    if dbtype == "sqlite": 
        try:
            retvalue = sqlitedb.create_table()
        except Exception as e:
            print(e)
    return retvalue


def insert_data(windowname,windowtitle,usedtime):
    global dbtype
    if dbtype == "sqlite": 
        try:
            sqlitedb.insert_data(windowname,windowtitle,usedtime)
        except Exception as e:
            print(e)


def select_all_data():
    global dbtype
    if dbtype == "sqlite": 
        try:
            sqlitedb.select_all_data()
        except Exception as e:
            print(e)

