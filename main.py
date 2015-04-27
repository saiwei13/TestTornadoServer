# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import datetime

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import logging
import json
import torndb
import chat
import file_handler
import os
import utils

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="db host")
define("mysql_database", default="tornado", help="db name")
define("mysql_user", default="chenwei", help="db user")
define("mysql_password", default="123456", help="db password")

logger = logging.getLogger('demo')

class MainHandler(tornado.web.RequestHandler):
    # def get(self,input):
    #     # logging.info("get()  input= %s"  % input );
    #     logging.info("get()");
    #     self.write("Hello, world, get method\n")

    def get(self, *args, **kwargs):
        logging.info("get()");

        # db = self.application.db
        #
        # todos = db.query("select * from user")
        # print todos
        # if not todos:
        #     return None
        # try:
        #
        # except Exception:
        #     print 'exception'
        #     return Err
        # finally:
        #     print 'finally'


        # self.write("Hello, world, get method\n  %d  %s" % (len(todos),todos));
        # self.write("hello world,get method\n")

    def post(self, *args, **kwargs):
        logging.info(" !!!");

        # tmp = self.get_body_argument('text1');
        # tmp = self.geta
        # tmp = self.request
        # tmp = self.get_argument('text1',default='No things')
        # tmp = self.get_query_argument('text1',default='No things')
        # tmp = self._request_summary()

        # data = json.loads(self.request.body.decode('utf-8'))

        data = self.request.body

        # args = self.request.arguments
        tt = self.get_argument('role');
        # for a in args:
        #     tt = self.get_argument(a)

        logging.info("args = %s " % tt);
        logging.info("args = %s " , tt);
        logging.info("args = %d " % len(tt));
        logging.info("args = %s %d" , tt,len(tt));
        logging.info("args = %s %d" % (tt ,len(tt)));

        logging.info("post() post %s " % data);

        self.finish("data: data --------%s \n" % data);
        # self.write("hello,world , post method\n")


table_name = 'user'

class RegisterHandler(tornado.web.RequestHandler):
    '''
    注册操作
    '''
    def get(self):
        logging.info('RegisterHandler  get()')

    def post(self):
        # logging.getLogger('demo').info('RegisterHandler  post()')
        # logging.info('RegisterHandler  post()')

        logger.info('RegisterHandler  post()')

        message =  self.request.body
        # print message
        # print type(message)

        # print self.request
        message = tornado.escape.json_decode(message)
        logger.info(message)
        # print message
        # print 'msg = ' , msg;
        # username = msg.username
        # print msg.userid

        # print type(msg)

        # print message['username']

        db = self.application.db
        sql = "select * from %s where username='%s'" % (table_name,message['username'])
        row = db.get(sql)
        if not row:
            print "未注册"
            userid = utils.md5(utils.showTime())
            sql = "insert into user (userid,username,pwd) values('%s','%s','%s')" \
                  % (userid,message['username'],message['pwd']);
            db.execute(sql)

            self.write('注册成功！');
        else:
            print "已注册"
            self.write('亲，账号已被注册！');

class LoginHandler(tornado.web.RequestHandler):
    '''
    登陆操作
    '''
    def get(self):
        self.post()

    def post(self):
        print "LoginHandler post"

        message = tornado.escape.json_decode(self.request.body)
        logger.info(message)

        sql = "select * from %s where username='%s'" % (table_name,message['username'])
        row = self.application.db.get(sql)

        print row

        if not row:
            self.write('用户名不存在，请重新输入')
        else:
            passwd = row['pwd']
            if passwd == message['pwd']:
                self.write('亲，登陆成功！')
            else:
                self.write('密码不正确')
        # self.redirect('/login')


class LogoutHandler(tornado.web.RequestHandler):
    '''
    注销操作
    '''
    def get(self):
        self.post()

    def post(self):
        self.end_session()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/register", RegisterHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
            (r"/upload", file_handler.UploadFileHandler),
            # (r"/download/([a-z]*)", DownloadFileHandler),
            (r"/download", file_handler.DownloadFileHandler),
            # (r"/websocket", EchoWebSocket),
            # (r"/websocket", ChatSocketHandler),
            (r"/websocket",chat.ChatSocketHandler ),
        ]
        settings = dict();
        tornado.web.Application.__init__(self,handlers,settings)
        self.db = torndb.Connection(
            host = options.mysql_host,
            database = options.mysql_database,
            user = options.mysql_user,
            password = options.mysql_password
        )

        LOGDIR = os.path.join(os.getcwd(),'log')
        LOGFILE = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.log'
        logging.basicConfig(level=logging.DEBUG,
                            format='',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename = os.path.join(LOGDIR,LOGFILE),
                            filemode='a'
                            )

        fileLog = logging.FileHandler(os.path.join(LOGDIR,LOGFILE),'w')
        formatter = logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s')
        fileLog.setFormatter(formatter)

        # logging.getLogger('demo').addHandler(fileLog)
        # logging.getLogger('demo').setLevel(logging.DEBUG)
        # logging.getLogger('demo').info(u'项目已启动：')

        logger.addHandler(fileLog)
        logger.setLevel(logging.DEBUG)
        logger.info(u'项目已启动：')

def main():
    tornado.options.parse_command_line()
    # application = tornado.web.Application([
    #     (r"/", MainHandler),
    #     (r"/register", RegisterHandler),
    #     (r"/upload", file_handler.UploadFileHandler),
    #     # (r"/download/([a-z]*)", DownloadFileHandler),
    #     (r"/download", file_handler.DownloadFileHandler),
    #     # (r"/websocket", EchoWebSocket),
    #     # (r"/websocket", ChatSocketHandler),
    #     (r"/websocket",chat.ChatSocketHandler ),
    # ])
    # http_server = tornado.httpserver.HTTPServer(application)
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
