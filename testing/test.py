from win32gui import GetForegroundWindow,GetWindowText
import psutil
import time
import win32process

process_time={}
timestamp = {}
while True:
    foregroundwnd = GetForegroundWindow()
    data = win32process.GetWindowThreadProcessId(foregroundwnd)[1]
    if psutil.pid_exists(data):
        print GetWindowText(foregroundwnd)
        current_app = psutil.Process(data).name().replace(".exe", "")
        timestamp[current_app] = int(time.time())
        time.sleep(1)
        if current_app not in process_time.keys():
            process_time[current_app] = 0
            process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
            print(process_time,process_time[current_app],timestamp[current_app],"\n")
    
    
