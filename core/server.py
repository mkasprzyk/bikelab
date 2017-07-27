import tornado.ioloop
import tornado.web


class UI(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def app(port, template_path, static_path):
    _app = tornado.web.Application([
        (r"/", UI),
        (r'/static', tornado.web.StaticFileHandler)
    ],
    template_path=template_path,
    static_path=static_path
    )
    _app.listen(port)
    tornado.ioloop.IOLoop.current().start()
