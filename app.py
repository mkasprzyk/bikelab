from cefpython3 import cefpython as cef
import threading
import sys

from core.server import app


CORE_PATH = "./core"
UI_PATH = "./ui"

class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        if not is_loading:
            pass

class Backend(object):
    def __init__(self, port):
        self.port = port
        self.thread = threading.Thread(target=app,
            args=(port, UI_PATH, UI_PATH)
        )

    def run(self):
        self.thread.start()


def main():
    sys.excepthook = cef.ExceptHook

    switches = {
        "ignore-gpu-blacklist": "true",
    }

    cef.Initialize(switches=switches)

    browser = cef.CreateBrowserSync(url="http://localhost:8123", window_title="BikeLab")
    browser.SetClientHandler(LoadHandler())

    backend = Backend(8123)
    backend.run()

    cef.MessageLoop()
    cef.Shutdown()


if __name__ == '__main__':
    main()
