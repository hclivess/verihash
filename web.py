import tornado.ioloop
import tornado.web
import json
from main import compare

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        pass

class WinHandler(tornado.web.RequestHandler):
    pass

class AllHandler(tornado.web.RequestHandler):
    def get(self, data):
        feed = data.split(";")
        print("feed",feed)
        self.write(json.dumps(compare(feed)))

def make_app():

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/win/(.*)", WinHandler),
        (r"/all/(.*)", AllHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(9091)
    tornado.ioloop.IOLoop.current().start()
