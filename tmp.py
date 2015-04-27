# -*- coding: utf-8 -*-

__author__ = 'chenwei'

from tornado import websocket


# class RegisterHandler(tornado.web.RequestHandler):
#     def post(self, *args, **kwargs):
#         print(self.request.body)
#         #解析android传过来的json
#         reg=json.loads(self.request.body.decode())
#         type=reg.get('type')
#         if(type=='child'):
#             childid=reg.get('childid')
#             parentid=reg.get('parentid')
#             password=reg.get('password')
#             resultcode=utils.register(childid,parentid,password)
#             self.write(resultcode)
#
#     def get(self):
#         # logging.info("get()  input= %s"  % input );
#         self.write("RegisterHandler, get method\n")


# class EchoWebSocket(tornado.websocket.WebSocketHandler):
#     def open(self):
#         print("WebSocket opened")
#         # self.write('i am server')
#
#     def on_message(self, message):
#         self.write_message(u"You said: " + message)
#         print("on_message  :  %s " %  message)
#
#     # def write_message(self, message, binary=False):
#     #     print "write_message"
#
#     def close(self, code=None, reason=None):
#         print "close";
#
#     def on_close(self):
#         print("WebSocket on_close")


# class ChatSocketHandler(tornado.websocket.WebSocketHandler):
#
#     waiters = set()
#     cache = []
#     cache_size = 200
#
#     @staticmethod
#     def send_to_all(message):
#         for c in ChatSocketHandler.waiters:
#             c.write_message(message);
#
#     def open(self):
#         print 'open ',id(self)
#
#         tmp = {'id':id(self),'msg':'Welcome to WebSocket'}
#
#         self.write_message(tmp)
#         # ChatSocketHandler.send_to_all()
#         ChatSocketHandler.send_to_all(str(id(self)) + ' has joined')
#         ChatSocketHandler.waiters.add(self);
#
# #        print ChatSocketHandler.waiters
# #         print id(self)
# #         print str(id(self))
#
#     def on_close(self):
#         print 'on_close', id(self)
#         ChatSocketHandler.waiters.remove(self);
#         ChatSocketHandler.send_to_all(str(id(self)) + ' has left')
#  #       print ChatSocketHandler.waiters
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
#         parsed = tornado.escape.json_decode(message)
#         chat={
#             "from":str(self),
#             "to":'',
#             "msg":parsed["msg"],
#         }
#
#         # chat["html"]=tornado.escape.to_basestring(
#         #     self.rend
#         # )
#
#         ChatSocketHandler.update_cache(chat)
#         ChatSocketHandler.send_updates(chat)
#
#     # def on_message(self, message):
#     #     logging.info("got message %r", message)
#     #     parsed = tornado.escape.json_decode(message)
#     #     chat = {
#     #         "id": str(uuid.uuid4()),
#     #         "body": parsed["body"],
#     #         }
#     #     chat["html"] = tornado.escape.to_basestring(
#     #         self.render_string("message.html", message=chat))
#     #
#     #     ChatSocketHandler.update_cache(chat)
#     #     ChatSocketHandler.send_updates(chat)


