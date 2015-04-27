__author__ = 'chenwei'
# -*- coding: utf-8 -*-
# filename = '/home/chenwei/tmp/sss'
# # open(filename,'rb')
# open("/home/chenwei/tmp/python_server.txt", 'wb')
#
# import os
# from os.path import getsize
#
# filename = "/home/chenwei/tmp/traces.txt";
#
# size = getsize(filename);
# print size

from tornado import escape
import logging
import json
import os

def test3():
    print os.getcwd()

def test2():
    row = 0;
    if not row:
        print 'tttt'

    if row is not None:
        print '!!!!'

def test1():
    id = 111;
    tmp = 'people [%d] has joined' % id


    print tmp

def test():
    # str = '{"__complex__": true, "real": 1, "imag": 2}'
    # parsed = escape.json_decode(str)
    # print 'str = ', str
    # print 'parsed  = ', parsed

    print '---------------------'
    message = '{"people1":"图腾"}'
    # str = '{"people1":"1234"}'
    # str ='{"people1":"\u56fe\u817e"}'
    parsed = escape.json_decode(message)
    print 'str = ', str
    print 'parsed  = ', parsed

    print '---------------------'

    logging.info("got message %r ",message);
    logging.info("got message %s ",message);

    ss = {
        'type': 'sys',
        'message':' has left'
    }


    print ss
    # print json.dump(ss)

def main():
    # logging.basicConfig(filename='myapp.log',filemode='w', level=logging.INFO)
    logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
    logging.info('Started')
    logging.info('Finished')

if __name__ == '__main__':
    main()
    # test()
    # test1()
    # test2()
    test3()
    import utils
    print utils.showTime()

    import os
    LOGDIR = os.path.join(os.getcwd(),'log')
    import datetime
    print datetime.datetime.now().strftime('%Y%m%d%H%M%S')