from cefpython3 import cefpython as cef
import threading
import sys
import os

from core.server import app



CORE_PATH = "core"
UI_PATH = "ui"


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        if not is_loading:
            pass

class Backend(object):
    def __init__(self, port):
        self.port = port
        self.thread = threading.Thread(target=app,
            args=(port, resource_path(UI_PATH), resource_path(UI_PATH))
        )

    def run(self):
        self.thread.start()

    def message(self, value, js_callback=None):
        if js_callback:
            js_callback.Call(value)
        return value

def main():
    sys.excepthook = cef.ExceptHook

    switches = {
        "ignore-gpu-blacklist": "true",
    }

    settings = {
        "resources_dir_path": resource_path('.'),
        "locales_dir_path": resource_path('locales'),
    }

    cef.Initialize(settings, switches=switches)
    backend = Backend(8123)

    bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)
    bindings.SetFunction("message", backend.message)

    browser = cef.CreateBrowserSync(url="http://localhost:8123", window_title="BikeLab")
    browser.SetJavascriptBindings(bindings)
    browser.SetClientHandler(LoadHandler())

    backend.run()
    cef.MessageLoop()
    cef.Shutdown()


if __name__ == '__main__':
    main()
