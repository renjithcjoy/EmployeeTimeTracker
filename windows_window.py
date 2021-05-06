import wmi
import win32gui
import win32process
import pythoncom

c = wmi.WMI()

"""
Much of this derived from: http://stackoverflow.com/a/14973422/965332
"""

def get_app_path(hwnd):
    """Get application path given hwnd."""
    path = None
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    for p in c.query('SELECT ExecutablePath FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
        path = p.ExecutablePath
        break
    return path

def get_app_name(hwnd):
    """Get application filename given hwnd."""
    name = None
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    for p in c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
        name = p.Name
        break
    return name

def get_window_title(hwnd):
    return win32gui.GetWindowText(hwnd)

def get_active_window_handle():
    hwnd = win32gui.GetForegroundWindow()
    return hwnd