# -*- coding: utf-8 -*-
import logging
import tornado.websocket


__author__ = 'chenwei'
##系统通知
system_id = 1000;
room_name = "私人空间"
room_id = 1111

# type    open  1
# type    system_notify  2
# type    chat  3

# class ChatSocketHandler(tornado.websocket.WebSocketHandler):
#     """
#     chat socket server
#     """
#     waiters = set()
#     cache = []
#     cache_size = 200
#
#     def get(self, *args, **kwargs):
#         print "ChatSocketHandler  get()"
#
#         # print self.request
#         #
#         # headers = self.request.headers
#         # username = headers['username']
#         # pwd = headers['pwd']
#         # print 'username = ',username
#         # print 'pwd = ',pwd
#         #
#         # self.write('sdfsdfkldsjfklsjdflskdfj');
#
#         super(ChatSocketHandler,self).get();
#
#         # super.__get__();
#         # super.__get__();
#
#     #
#     #通知所有人员
#     #
#     @staticmethod
#     def send_to_all(message):
#         tmp = {
#             'type':2,
#             'id':system_id,
#             "msg":message,
#             'count':len(ChatSocketHandler.waiters)
#         }
#         for c in ChatSocketHandler.waiters:
#             c.write_message(tmp);
#
#     def open(self):
#         print 'open ',id(self)
#         ChatSocketHandler.waiters.add(self);
#
#         tmp = {
#             'type':1,
#             'id':id(self),
#             'msg':'Welcome to WebSocket',
#             'room_name':room_name,
#             'count':len(ChatSocketHandler.waiters)
#         }
#         self.write_message(tmp)
#
#         tmp = 'people [%d] has joined' % id(self)
#
#         ChatSocketHandler.send_to_all(tmp)
# #        print ChatSocketHandler.waiters
# #         print id(self)
# #         print str(id(self))
#
#     def on_close(self):
#         print 'on_close', id(self)
#         ChatSocketHandler.waiters.remove(self);
#
#         tmp = 'people [%d] has left' % id(self)
#         ChatSocketHandler.send_to_all(tmp)
#
#     @classmethod
#     def update_cache(cls, chat):
#         cls.cache.append(chat)
#         if len(cls.cache) > cls.cache_size:
#             cls.cache = cls.cache[-cls.cache_size:]
#
#     @classmethod
#     def send_updates(cls, chat):
#         logging.info("sending message to %d waiters", len(cls.waiters))
#         for waiter in cls.waiters:
#             try:
#                 waiter.write_message(chat)
#             except:
#                 logging.error("Error sending message", exc_info=True)
#
#     def on_message(self, message):
#         logging.info("got message %r ",message);
#         chat = tornado.escape.json_decode(message)
#         # chat={
#         #     "from":str(self),
#         #     "to":'',
#         #     "msg":parsed["msg"],
#         # }
#         ChatSocketHandler.update_cache(chat)
#         ChatSocketHandler.send_updates(chat)
#
#     def ping(self, data):
#         print 'ping'
#     def on_pong(self, data):
#         print 'on_pong'



class PushHandler(tornado.web.RequestHandler):

    def post(self):

        # body =  self.request.body
        # print body;
        # print type(body)
        body=tornado.escape.json_decode(self.request.body)
        # print body
        msg = body['msg']
        print 'PushHandler  msg = ',msg
        if not msg :
            pass
        else :
            PushSocketHandler.send_to_all(msg);
    def get(self):
        logging.info("get()");

        print self.request
        print self.request.body

        self.write('hello world');

        # chat.PushSocketHandler.send_to_all('通知所有手机');



class PushSocketHandler(tornado.websocket.WebSocketHandler):
    """
    chat socket server
    """
    waiters = set()
    cache = []
    cache_size = 200

    def get(self, *args, **kwargs):
        print "PushSocketHandler  get()"
        # print self.request
        # headers = self.request.headers
        # username = headers['username']
        # pwd = headers['pwd']
        # print 'username = ',username
        # print 'pwd = ',pwd

        super(PushSocketHandler,self).get();

    #
    #通知所有人员
    #
    @staticmethod
    def send_to_all(message):
        tmp = {
            'type':2,
            'id':system_id,
            "msg":message,
            'count':len(PushSocketHandler.waiters)
        }
        for c in PushSocketHandler.waiters:
            c.write_message(tmp);

    def open(self):
        print 'open ',id(self)
        PushSocketHandler.waiters.add(self);
#        print ChatSocketHandler.waiters
#         print id(self)
#         print str(id(self))

    def on_close(self):
        print 'on_close', id(self)
        PushSocketHandler.waiters.remove(self);


class LocationSocketHandler(tornado.websocket.WebSocketHandler):
    """
    更新位置信息
    协议：
    有ｇｐｓ数据
    {
        "rspcode":"0000",
        "location": {
            "lat": 51.0,
            "lng": -0.1
        },
        "accuracy": 1200.4
    }

    无ｇｐｓ数据
    {
        "rspcode":"000１"
    }
    """
    waiters = set()
    cache = []
    cache_size = 200

    def check_origin(self, origin):
        return True;

    def get(self, *args, **kwargs):


        print "LocationSocketHandler  get()"

        print self.request
        print self.request.body

        super(LocationSocketHandler,self).get();

    def open(self):
        print 'open ',id(self)

        self.write_message('hello world from server');

        LocationSocketHandler.waiters.add(self);

    def on_close(self):
        print 'on_close', id(self)
        LocationSocketHandler.waiters.remove(self);

    def on_message(self, message):
        print 'on_message'
        print message










