import sys
import json

"""
def get_current_window_linux():
    from . import xlib
    window = xlib.get_current_window()

    if window is None:
        cls = "unknown"
        name = "unknown"
    else:
        cls = xlib.get_window_class(window)
        name = xlib.get_window_name(window)

    return {"appname": cls, "title": name}


def get_current_window_macos():
    from . import macos
    info = macos.getInfo()
    app = macos.getApp(info)
    title = macos.getTitle(info)

    return {"title": title, "appname": app}

"""
def get_current_window_windows():
    import windows
    window_handle = windows.get_active_window_handle()
    app = windows.get_app_name(window_handle)
    title = windows.get_window_title(window_handle)

    if app is None:
        app = "unknown"
    if title is None:
        title = "unknown"

    return {"appname": app, "title": title}


def get_current_window():
    if sys.platform in ["win32", "cygwin"]:
        return get_current_window_windows()
    else:
        raise Exception("Unknown platform: {}".format(sys.platform))



def get_current_idle_time_windows():
    import windows
    idletime = windows.seconds_since_last_input()
    return idletime


def get_current_idle_time():
    if sys.platform in ["win32", "cygwin"]:
        return get_current_idle_time_windows()
    else:
        raise Exception("Unknown platform: {}".format(sys.platform))
