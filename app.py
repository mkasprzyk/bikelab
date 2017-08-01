from cefpython3 import cefpython as cef
import threading
import sys
import os

from core.server import app
import settings


class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        if not is_loading:
            pass

class Backend(object):
    def __init__(self, port):
        self.port = port
        self.thread = threading.Thread(target=app,
            args=(port, settings.UI_PATH, settings.UI_PATH)
        )

    def run(self):
        self.thread.start()

    def message(self, value, js_callback=None):
        if js_callback:
            js_callback.Call(value)
        return value

def main():
    sys.excepthook = cef.ExceptHook

    cef.Initialize(settings.cef_settings, switches=settings.cef_switches)
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
