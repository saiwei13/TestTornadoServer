# -*- coding: utf-8 -*-
__author__ = 'chenwei'


import logging


def md5(str):
    '''
    md5 加密
    :param str:
    :return:
    '''
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def showTime():
    '''
    显示时间
    :return:
    '''
    import time
    cur_time = int(time.time());
    return str(cur_time)


def register(childid,parentid,password):

    logging.info('register  childid=%s  parentid=%s password=%s' % (childid,parentid,password))

    if(childid == 'chenwei' and password=='123456'):
        return 'ok';
    else:
        return 'fail';

    # #连接数据库
    # cnx = mysql.connector.connect(user=MysqlConInfo[0], password=MysqlConInfo[1], host=MysqlConInfo[2],
    #                               database=MysqlConInfo[3], charset='utf8')
    # cursor = cnx.cursor()
    # y="select * from careparents.userinfo where childid='%s'" %(childid)
    # cursor.execute(y)
    # res = cursor.fetchall()
    # print(res)
    # print(len(res))
    # if(len(res)!=0):
    #     resultcode={'result':'0'}
    #     #将json格式数据转化为字符串返回给android
    #     return json.dumps(resultcode,ensure_ascii=False)
    #     #return '0'
    #     #return 'sorry,这个账号已经被注册了'
    # x="insert into careparents.userinfo (childid, parentid, password) values ('%s','%s','%s')" % (childid,parentid,password)
    # cursor.execute(x)
    # cursor.close()
    # cnx.commit()
    # cnx.close()
    # print(childid+'---'+parentid+'---register')
    # resultcode={'result':'1'}
    # return json.dumps(resultcode,ensure_ascii=False)