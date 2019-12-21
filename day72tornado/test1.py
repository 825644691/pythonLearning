import tornado.web
import tornado.ioloop


class Base:
    def initialize(self):
        # 获取用户cookie，如果有不操作，否则给用户生成随机字符串
        # 写给用户
        # 保证session
        from session import Session
        self.session = Session(self)
        super(Base, self).initialize()


class BaseHandler(tornado.web.RequestHandler):
    #blog.csdn.net/moshowgame 解决跨域问题
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', '*')
        self.set_header('Access-Control-Allow-Headers','*')


class MainHandler(Base, BaseHandler):
    def get(self):
        if self.session['login']:
            print(self.session['login'])
            print('helloworld')


        #获取参数
        # v = self.get_argument('p')  # get 和post都是这个
        # self.request 封装了请求的相关信息

class LoginHandler(Base, BaseHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        v = self.get_argument('user')
        if v == 'root':
            self.session['login'] = True
            # self.redirect('/index')
        else:
            print('error')

application = tornado.web.Application(
    [
        ('/index', MainHandler),
        ('/login', LoginHandler)
    ]
)


if __name__ == '__main__':
    # 创建socket对象8888
    # 将socket对象添加到select或epoll中
    application.listen(8888)
    print(1)
    #将select或者epoll开始死循环 while True
    tornado.ioloop.IOLoop.instance().start()


