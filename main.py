from time import sleep
from Queue import Queue
import time
import datetime
import pytz
import threading
import sys
import signal

import lib
import db

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def main():
    try:
        q = Queue()

        signal.signal(signal.SIGINT, signal_handler)

        currentwindowthread = threading.Thread(target=window_heartbeat_loop, args=(q,1,False,))
        currentwindowthread.daemon = True
        idlewindowthread = threading.Thread(target=idle_heartbeat_loop, args=(1,))
        idlewindowthread.daemon = True
        dbthread = threading.Thread(target=dbthreadfn, args=(q,))
        dbthread.daemon = True

        currentwindowthread.start()
        idlewindowthread.start()
        dbthread.start()
    except Exception as e:
        print("Main exception  ",e)
        sys.exit("Error message")



    while True:
       sleep(1)
        

def window_heartbeat_loop(out_q,poll_time,exclude_title=False):
    print("window_heartbeat_loop")
    previousdata =  {}
    while True:
        try:
            current_window = lib.get_current_window()
        except Exception as e:
            print("Exception thrown while trying to get active window: {}".format(e))
            current_window = {"appname": "unknown", "title": "unknown"}
            
        now = datetime.datetime.now(pytz.utc)
        if current_window is None:
            print('Unable to fetch window, trying again on next poll')
        else:
            # Create current_window event
            data = {
                "timestamp":now,
                "app": current_window["appname"],
                "title": current_window["title"] if not exclude_title else "excluded"
            }

            if current_window["appname"] not in previousdata.values() and current_window["title"] not in previousdata.values():
                Printdata(out_q,previousdata)
                previousdata.clear()
                previousdata["starttime"] = time.time()
                previousdata["timestamp"] = data.get("timestamp")
                previousdata["app"] = data.get("app")
                previousdata["title"] = data.get("title")
                
                
                
        sleep(poll_time)



def Printdata(out_q,data):
    if len(data) > 0:
        data["usedtime"] = time.time() - data.get("starttime")
        print("Inserted to queue   ",data)
        out_q.put(data)
        #db.insert_data(data.get("app"),data.get("title"),data.get("usedtime"))
        #print(data)


def idle_heartbeat_loop(poll_time):
    print("idle_heartbeat_loop")
    while True:
        try:
            current_idletime = lib.get_current_idle_time()
            print(current_idletime)
            sleep(poll_time)
        except Exception as e:
            print("idle_heartbeat_loop exception  ",e)
            sys.exit("Error message")
        

def dbthreadfn(in_q):
    db.create_table()
    while True:
        try:
            data = in_q.get()
            print("Get data from queue   ",data)
            db.insert_data(data.get("app"),data.get("title"),data.get("usedtime"))
        except Exception as e:
            print("dbthreadfn exception  ",e)
            sys.exit("Error message")



if __name__ == "__main__":
    main()