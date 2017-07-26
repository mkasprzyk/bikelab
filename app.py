from cefpython3 import cefpython as cef
import platform
import sys



UI_HTML = open('ui/index.html')
UI_JS = open('ui/js/opejscad.min.js')

def html_to_data_uri(html, js_callback=None):
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html.read()).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    if js_callback:
        js_callback.Call(ret)
    else:
        return ret

class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        if not is_loading:
            browser.ExecuteJavascript(UI_JS.read())

def main():
    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    cef.CreateBrowserSync(url=html_to_data_uri(UI_HTML), window_title="BikeLab")
    cef.MessageLoop()
    cef.Shutdown()


if __name__ == '__main__':
    main()
