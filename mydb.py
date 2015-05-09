# -*- coding: utf-8 -*-

__author__ = 'chenwei'

#
# 操作数据库
#

import torndb
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
    print  cur_time

print  type(md5(str(showTime())))

# if 1:
#     print "1 true"
# if 0:
#     print '0 true'
# db = torndb.Connection("localhost", "tornado","chenwei","123456")
#
# db.execute("insert into user (userid,username) values(5,'chenwei')")

table_name = 'user'

db = torndb.Connection("localhost", "tornado","chenwei","123456")

try:
    print md5(str(1));
    # raise Exception('spam', 'eggs')
    # raise Exception('chenwi')


    #

    #select
    # sql = "SELECT * FROM {table_name} WHERE userid = %(userid)d".format(
    # table_name='user')

    # sql = "SELECT * FROM user WHERE userid = 3"
    #
    # if sql:
    #     print 'have'
    # else:
    #     print 'else'
    #
    #
    # row = db.query(sql)
    #
    # if row:
    #     print 'sss'
    # else:
    #     print 'nonono'
    #
    # if not row:
    #     print 'tttt'
    #
    # if row is not None:
    #     print '!!!!'
    #
    # print len(row)
    # print row
    # print row[0]['username']

    #update


    #delect


    #create
    # cre='create table user (id int,content text)'
    # db.execute(cre);

    # db.execute("insert into user (userid, sid,username,pwd) values('%s', %s,)",
    #         4,'sss')
    # db.execute("insert into user (userid) values(4)")
    # db.execute("insert into user (userid) values(4)")
    # db.execute("insert into user (userid,username) values(5,'chenwei')")
    # db.execute("insert into user (userid,username) values(5,'chenwei')")


    # sql = "SELECT * FROM {table_name} WHERE userid = %(userid)d".format(
    # table_name=table_name)
    # db.get(sql,4);
    # for post in db.query("SELECT * FROM user limit 1"):
    #     print  type(post)
    #     print post
    #     print post.userid
    #
    # post = db.get("SELECT * FROM user limit 1")
    # print  type(post)
    # print post
    # # print post.userid
    # # print post['pwd']
    # print post.get('pwd')
    #
    # post = {'userid':'222','pwd':'cw','username':'cw'}
    # print type(post)
    # print post
    # print post.get('userid')
    # print post['userid']


    # for post in db.get("SELECT * FROM user limit 1"):
    #     print post
    #     print post.userid

    # print db.get("SELECT * FROM user limit 1")

    #insert
    # uid = insert(table_name, {'username': 'david', 'pwd': 'abc'})
    # db.execute("insert into user (username,pwd) values('chenwei','abc')")

    # db.execute("insert into user (username,pwd) values('chenwei','abc')")

    # sql = "insert into user (userid,username,pwd) values('%s','%s','%s')" % (str(5),"chenwei","abc");
    # sql ="insert into user (userid,username,pwd) values(1,'chenwei','abc')"
    # sql = "insert into user (userid,username,pwd) values(%s,%s,%s)"
    # print sql
    # db.execute(sql,str(3),'chenwei','abc')
    # row = db.execute(sql)
    # print row

    # sql = "insert into apk (package_name,version_code,version_name,url) values('%s',%s,'%s','%s')" % ('com.example.chenwei.testsocket',2,'1.2','download_apk');
    # db.execute(sql)

    # for i in range(1, 5):
    #     print i
    #     db.execute("insert into user (userid,username,pwd) values(%s,%s,%s)"  ,md5(str(i)),'chenwei','abc',)

    # db.execute(sql)

    #delete
    # db.execute("delete from user where userid=5")
    # db.execute("delete from apk")

    #
    # db.execute("update user set username='cc' where userid='5'")

    # db.execute("update user set username='chenwei' where username='bb'")

except IOError:
    print 'ioerror'

except Exception as e:
    print 'exception'
    logging.exception(e)
    # logging.info(e)
    # print type(e)
    # print e.args
    print e
    # print 'connect fail '
except:
    print 'ddd'
else:
    print 'else'
finally:
    print 'finally'




