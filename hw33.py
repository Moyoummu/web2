import tornado.web
import tornado.ioloop
import tornado.httpserver
import os

req_counter = 0

class htmlHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('h2.html')

class RequestCountHandler(tornado.web.RequestHandler):
    def get(self):
        global req_counter
        req_counter += 1
        self.write(f'Номер запроса:  {req_counter}')

class webApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', htmlHandler),
            (r'/#request', RequestCountHandler),
            (r'/(.*)', tornado.web.StaticFileHandler, {'path': os.path.abspath(__file__)})

        ]
        tornado.web.Application.__init__(self, handlers)

if __name__ == '__main__':
    w_app = webApp()
    server = tornado.httpserver.HTTPServer(w_app)
    server.listen(8888)
    print('Listening')
    tornado.ioloop.IOLoop.current().start()