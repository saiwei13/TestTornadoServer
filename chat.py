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

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    """
    chat socket server
    """
    waiters = set()
    cache = []
    cache_size = 200

    #
    #通知所有人员
    #
    @staticmethod
    def send_to_all(message):
        tmp = {
            'type':2,
            'id':system_id,
            "msg":message,
            'count':len(ChatSocketHandler.waiters)
        }
        for c in ChatSocketHandler.waiters:
            c.write_message(tmp);

    def open(self):
        print 'open ',id(self)
        ChatSocketHandler.waiters.add(self);

        tmp = {
            'type':1,
            'id':id(self),
            'msg':'Welcome to WebSocket',
            'room_name':room_name,
            'count':len(ChatSocketHandler.waiters)
        }
        self.write_message(tmp)

        tmp = 'people [%d] has joined' % id(self)

        ChatSocketHandler.send_to_all(tmp)
#        print ChatSocketHandler.waiters
#         print id(self)
#         print str(id(self))

    def on_close(self):
        print 'on_close', id(self)
        ChatSocketHandler.waiters.remove(self);

        tmp = 'people [%d] has left' % id(self)
        ChatSocketHandler.send_to_all(tmp)

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r ",message);
        chat = tornado.escape.json_decode(message)
        # chat={
        #     "from":str(self),
        #     "to":'',
        #     "msg":parsed["msg"],
        # }
        ChatSocketHandler.update_cache(chat)
        ChatSocketHandler.send_updates(chat)

    def ping(self, data):
        print 'ping'
    def on_pong(self, data):
        print 'on_pong'

