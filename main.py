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
import test
import utils
import time
import base64
import uuid

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="db host")
define("mysql_database", default="tornado", help="db name")
define("mysql_user", default="chenwei", help="db user")
define("mysql_password", default="123456", help="db password")

logger = logging.getLogger('demo')

table_name = 'user'


class MainHandler(tornado.web.RequestHandler):
    # def get(self,input):
    #     # logging.info("get()  input= %s"  % input );
    #     logging.info("get()");
    #     self.write("Hello, world, get method\n")

    def get(self, *args, **kwargs):
        logging.info("get()");

        self.write('hello world post')
        self.render('index2.html')
        # self.render('test.html')

        #
        # print self.request
        # print self.request.body
        #
        # self.write('hello world');

        # self.render('index.html',title='')
        # self.redirect('index.html')

        # self.render('index.html',title='what is your name?')


        # chat.PushSocketHandler.send_to_all('通知所有手机');

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
        print ('post')
        print (self.request)
        print (self.request.body)
        self.write('hello world post')

        self.render('index.html')

        # logging.info(" !!!");

        # tmp = self.get_body_argument('text1');
        # tmp = self.geta
        # tmp = self.request
        # tmp = self.get_argument('text1',default='No things')
        # tmp = self.get_query_argument('text1',default='No things')
        # tmp = self._request_summary()

        # data = json.loads(self.request.body.decode('utf-8'))

        # data = self.request.body

        # args = self.request.arguments
        # tt = self.get_argument('role');
        # for a in args:
        #     tt = self.get_argument(a)

        # logging.info("args = %s " % tt);
        # logging.info("args = %s " , tt);
        # logging.info("args = %d " % len(tt));
        # logging.info("args = %s %d" , tt,len(tt));
        # logging.info("args = %s %d" % (tt ,len(tt)));
        #
        # logging.info("post() post %s " % data);
        #
        # self.finish("data: data --------%s \n" % data);
        # self.write("hello,world , post method\n")



class RegisterHandler(tornado.web.RequestHandler):
    '''
    注册操作
    '''
    def get(self):
        logging.info('RegisterHandler  get()')
        # print self.request
        # print self.request['host']
        # print self.get_argument('host')
        # print self.request.headers

        # print self.request.host
        # print type(self.request)
        # print self.request
        # print self.request.headers['host']
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
            print ("未注册")
            userid = utils.md5(utils.showTime())
            sql = "insert into user (userid,username,pwd) values('%s','%s','%s')" \
                  % (userid,message['username'],message['pwd']);
            db.execute(sql)

            self.write('注册成功！');
        else:
            print ("已注册")
            self.write('亲，账号已被注册！');

class LoginHandler(tornado.web.RequestHandler):
    '''
    登陆操作
    '''
    def get(self):
        self.post()

    def post(self):
        print ("LoginHandler post")

        message = tornado.escape.json_decode(self.request.body)
        logger.info(message)

        sql = "select * from %s where username='%s'" % (table_name,message['username'])
        row = self.application.db.get(sql)

        print (row)

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

class Update(tornado.web.RequestHandler):
    '''
    检查最新版本
    json协议：　　{'package_name':'xxx','version_code':'xx','version_name':'xxxx'}
    rspcode: 0000    有更新版本，提供ａｐｋ信息
    rspcode: 0001　　　无更新版本
    rspcode: 0002　　　服务器无该ａｐｋ
    '''
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        print( 'CheckUpdateVerion()')
        msg = tornado.escape.json_decode(self.request.body)
        print (msg)
        package_name = msg['package_name']
        version_code = msg['version_code']

        print ('package_name = ',package_name)
        sql = "select * from %s where package_name='%s'" % ('apk',package_name);
        row = self.application.db.get(sql)
        print ('version_code=',version_code)
        print ('last_version_code=',row['version_code'])
        if not row:
            print ('rspcode 0002')
            self.write({
                'rspcode':'0002',
                'msg':'服务器无该ａｐｋ',
                })
        elif int(row['version_code']) < int(version_code):
            print ('rspcode 0001')
            self.write({
                'rspcode':'0001',
                'msg':'该ａｐｋ已经是最新版本，不需要更新',
                })
        else:
            print ('rspcode 0000')
            self.write({
                'rspcode':'0000',
                'package_name':row['package_name'],
                'version_code':row['version_code'],
                'version_name':row['version_name'],
                'url':row['url'],
                'msg':'有最新版本',
                })

from os.path import getsize

class DownloadApk(tornado.web.RequestHandler):
    '''
    下载最新版本
    '''

    def download(self,filename):
        print('download()')

        if not filename:
            print ('filename is null')
            return

        size = 0;
        size = getsize(filename);

        #Content-Type这里我写的时候是固定的了，也可以根据实际情况传值进来
        self.set_header ('Content-Type', 'application/octet-stream')
        self.set_header ('Content-Disposition', 'attachment; filename='+filename)
        self.set_header ('length',size)

        #读取的模式需要根据实际情况进行修改
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024*1024*1)   #4096
                if not data:
                    break
                self.write(data)
        #记得有finish哦
        self.finish()
        print( 'finish')

    def get(self):
        pass

    def post(self):

        # msg = tornado.escape.json_decode(self.request.body)
        # print msg
        # url = msg['url']
        # print "url = ",url

        print('post() i download file handler : ')

        msg = tornado.escape.json_decode(self.request.body)
        package_name = msg['package_name']

        filename = "/home/chenwei/tmp/%s/%s.apk" % (package_name,package_name);
        self.download(filename)


class Application(tornado.web.Application):
    def __init__(self):

        cookie_secret_key = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)

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
            # (r"/websocket",chat.ChatSocketHandler ),
            (r"/push",chat.PushSocketHandler ),
            (r"/pushmsg",chat.PushHandler ),
            (r"/update",Update ),
            (r"/download_apk",DownloadApk ),
            (r"/location_ws",chat.LocationSocketHandler ),

            (r"/test",test.MainHandler ),
            (r"/test_login",test.LoginHandler ),
            (r"/test_loginout",test.LogoutHandler ),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret=cookie_secret_key,
            xsrf_cookies=True,
            login_url='/test_login',
        );
        tornado.web.Application.__init__(self,handlers,**settings)
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
        # logger.info(u'项目已启动：')

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()