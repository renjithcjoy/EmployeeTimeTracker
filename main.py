from time import sleep
import datetime
import pytz
import threading

import lib


def main():
    currentwindowthread = threading.Thread(target=window_heartbeat_loop, args=(1,False,))
    currentwindowthread.daemon = True
    idlewindowthread = threading.Thread(target=idle_heartbeat_loop, args=(1,))
    idlewindowthread.daemon = True

    currentwindowthread.start()
    idlewindowthread.start()

    while True:
        sleep(1)
        

def window_heartbeat_loop(poll_time,exclude_title=False):
    print("window_heartbeat_loop")
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
            Printdata(data)    
        sleep(poll_time)



def Printdata(data):
    print(data)


def idle_heartbeat_loop(poll_time):
    print("idle_heartbeat_loop")
    while True:
        current_idletime = lib.get_current_idle_time()
        print(current_idletime)
        sleep(poll_time)
        




if __name__ == "__main__":
    main()