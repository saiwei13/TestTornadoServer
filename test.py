# -*- coding: utf-8 -*-
import tornado
import tornado.web

__author__ = 'chenwei'

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class TestHandler(tornado.web.RequestHandler):
    '''
    测试　cookie
    '''
    def get(self, *args, **kwargs):
        print ('get')
# 'Cookie': 'csrftoken=BU0nXxBACETTBWQ9bDrtoMTlptwtFdnb'
# 'Cookie': 'csrftoken=BU0nXxBACETTBWQ9bDrtoMTlptwtFdnb; mycookie=myvalue'
        print (self.request)

        # self.get_secure_cookie("username")

        if not self.get_secure_cookie('mycookie'):
            self.set_secure_cookie('mycookie','myvalue')
            self.write("Your secure cookie was not set yet!")
        else :
            cookie = self.get_secure_cookie('mycookie')
            print("cookie=%s" % cookie)
            print (type(cookie))

            self.write("Your secure cookie was set!")
        # if not self.get_cookie("mycookie"):
        #     self.set_cookie("mycookie", "myvalue")
        #     self.write("Your cookie was not set yet!")
        # else:
        #     # c = self.get_cookie();
        #     # self.clear_cookie('mycookie')
        #     # print c
        #     self.write("Your cookie was set!")

    def post(self, *args, **kwargs):
        print ('post')


class MainHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self,*args, **kwargs):
        # print self.request
        # name = tornado.escape.xhtml_escape(self.current_user)
        name = self.current_user
        self.write("Hello, " + name)

    def post(self, *args, **kwargs):
        print ('post()')

class LoginHandler(BaseHandler):
    def get(self):

        self.render('test.html')

    def post(self):

        username = self.get_argument('username',default='');
        if not username:
            msg = "username is null"
            self.finish("<html><title>%(code)d: %(message)s</title>"
                        "<body>%(code)d: %(message)s</body></html>" % {
                            "code": 404,
                            "message": msg,
                        })
        else:
            # httponly = True, secure = Tru
            self.set_secure_cookie("username", username)
            self.redirect("/test")

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('username')
        self.redirect('/test')