# -*- coding: utf-8 -*-
import base64
import time
import uuid
import sys

__author__ = 'chenwei'

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
# import urllib2
import urllib
import re
import requests

url = "http://192.168.1.104:8888"

def testCreateCookis():
    base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    # OJqe5vbkTqq82DqpaCuyYlHEqoB6BEzWhDq2JTJ+iZI=
    # print uuid.uuid4()
    # 1275223e-d92b-499a-88a8-e2f777a71b83

# def testPushMsg(data):
#     '''
#     参考：　http://stackoverflow.com/questions/3290522/urllib2-and-json
#     http://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json
#     :param data:
#     :return:
#     '''
#     # data = json.dumps([1, 2, 3])
#     # print type(data)
#     # req = urllib2.Request('http://192.168.1.104:8888/pushmsg', json.dumps({'msg':'ddd'}), {'Content-Type': 'application/json'})
#     data={'msg':data}
#     req = urllib2.Request('http://192.168.1.104:8888/pushmsg', json.dumps(data))
#     f = urllib2.urlopen(req)
#     response = f.read()
#     f.close()
#     print response


# def testPost_3():
#     f = urllib2.urlopen(url,'sssssssssssssss')
#     print f.read


# def testPost_2():
#     req = urllib2.Request(url);
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
#     response = opener.open(req,'ddddddd')
#     print response.read()
#
# def testPost():
#     req = urllib2.Request(url);
#     req.add_header('aaa','bbb')     #添加表头　
#     req.add_data('tttttttttttttt')
#     f = urllib2.urlopen(req)
#     print f.read
#
# def testGet():
#     # url = "https://cas.bianfeng.com/authen/staticLogin.jsonp";
#     ##方法一
#     f = urllib2.urlopen(url)   #get request
#     print f.read(100)

    ##方法二
    # req = urllib2.Request("http://localhost:8888/test");
    # urllib2.urlopen(req)


def test3():
    print('当前路径：',os.getcwd())

def test2():
    row = 0;
    if not row:
        print('tttt')

    if row is not None:
        print('!!!!')

def test1():
    id = 111;
    tmp = 'people [%d] has joined' % id
    print(tmp)

def test():
    # str = '{"__complex__": true, "real": 1, "imag": 2}'
    # parsed = escape.json_decode(str)
    # print 'str = ', str
    # print 'parsed  = ', parsed

    print('---------------------')
    message = '{"people1":"图腾"}'
    # str = '{"people1":"1234"}'
    # str ='{"people1":"\u56fe\u817e"}'
    parsed = escape.json_decode(message)
    print('str = ', str)
    print ('parsed  = ', parsed)

    print ('---------------------')

    logging.info("got message %r ",message);
    logging.info("got message %s ",message);

    ss = {
        'type': 'sys',
        'message':' has left'
    }
    print (ss)
    # print json.dump(ss)

def testLog():
    '''
    测试ｌｏｇ
    '''
    # logging.basicConfig(filename='myapp.log',filemode='w', level=logging.INFO)
    logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
    logging.info('Started')
    logging.info('Finished')

# def testMockCookie():
#     '''
#     伪造cookie ,通过脚本去request
#     '''
#
#     req = urllib2.Request("http://localhost:8888/test");
#     # req.add_data('tttttttttttttt')
#     # req.add_header('Accept-Language','en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4')
#     # req.add_header('Accept-Encoding','gzip, deflate, sdch')
#     # req.add_header('Host','127.0.0.1:8888')
#     # req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
#     # req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36')
#     # req.add_header('Connection','keep-alive')
#     # req.add_header('Referer','http://127.0.0.1:8888/test_login')
#     # req.add_header('Cache-Control','max-age=0')
#     # req.add_header('If-None-Match','"066dbf52e76db6c9cb4ccc6b0b0192e040f34ccb"')
#     req.add_header('Cookie','_xsrf=2|ffac19ab|e978600371e519664208e174bc1057e4|1430673712; username="2|1:0|10:1430677645|8:username|12:Y2hlbndlaQ==|e78b6d0e27d66d6412240cc18c04c3b830a6a9d324b61369bf88c758af715115"')
#     f = urllib2.urlopen(req)
#
#     print f.read(100);
#
#     # 网页
#     # HTTPServerRequest(
#     #     protocol='http',
#     #     host='127.0.0.1:8888',
#     #     method='GET',
#     #     uri='/test',
#     #     version='HTTP/1.1',
#     #     remote_ip='127.0.0.1',
#     #     headers={
#     #         'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
#     #         'Accept-Encoding': 'gzip, deflate, sdch',
#     #         'Host': '127.0.0.1:8888',
#     #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     #         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36',
#     #         'Connection': 'keep-alive',
#     #         'Referer': 'http://127.0.0.1:8888/test_login',
#     #         'Cache-Control': 'max-age=0',
#     #         'Cookie': 'csrftoken=BU0nXxBACETTBWQ9bDrtoMTlptwtFdnb; username="2|1:0|10:1430668486|8:username|12:Y2hlbndlaQ==|db79086c9f97c938b18fc951a721ec502e3ecce7572a502eeb22bc147c9454fe"'})
#     #
#     # 脚本
#     # HTTPServerRequest(
#     #     protocol='http',
#     #     host='localhost:8888',
#     #     method='GET',
#     #     uri='/test',
#     #     version='HTTP/1.1',
#     #     remote_ip='127.0.0.1',
#     #     headers={
#     #         'Username': '2|1:0|10:1430668486|8:username|12:Y2hlbndlaQ==|db79086c9f97c938b18fc951a721ec502e3ecce7572a502eeb22bc147c9454fe', 'Host': 'localhost:8888', 'User-Agent': 'Python-urllib/2.7', 'Connection': 'close', 'Accept-Encoding': 'identity'})


def testMatch():
    '''
    测试　正则表达式
    '''

    #
    # pattern = re.compile(r'\D+')
    # match = pattern.match('hello world!')
    #
    # if match:
    #     print match.group()
    # else:
    #     print 'no match'

    # line = 'Cats are smarter than dogs'
    # matchObj = re.match(r'(.*)',line,re.M|re.I)
    # if matchObj:
    #     print 'matchObj.group() : ',matchObj.group()
    #     # print 'matchObj.group(1) : ',matchObj.group(1)
    #     # print 'matchObj.group(2) : ',matchObj.group(2)
    # else:
    #     print 'no match'


    # line = '2004-959-959 # this is phone number'
    # # num = re.sub(r'#.{3,}',"",line)
    # # num = re.sub(r'\D',"",line)
    # num = re.match(r'\d{3,}',line,re.M|re.I)
    # # print num.group()
    # print num.groups()

    # print re.DOTALL

    # m = re.match(r'\w+\s', 'hello worldsss!')
    # print "m.string:", m.string
    # print "m.re:", m.re
    # print "m.pos:", m.pos
    # print "m.endpos:", m.endpos
    # print "m.lastindex:", m.lastindex
    # print "m.lastgroup:", m.lastgroup

    # pattern = re.compile(r'world')
    #
    # # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
    # # 这个例子中使用match()无法成功匹配
    # match = pattern.search('hello world!')
    #
    # if match:
    #     # 使用Match获得分组信息
    #     print match.group()
    # p = re.compile(r'\d+')
    # print p.split('one1two2three3four4')
    #
    # print p.findall('one1two2three3four4')


    #
    # a = re.compile(r"""\d +  # the integral part
    #                    \.    # the decimal point
    #                    \d *  # some fractional digits""", re.X)
    #
    # b = re.compile(r"\d+\.\d*")
    #
    # match11 = a.match('3.1415')
    # match12 = a.match('33')
    # match21 = b.match('3.1415')
    # match22 = b.match('33')
    #
    # if match11:
    #     # 使用Match获得分组信息
    #     print match11.group()
    # else:
    #     print u'match11不是小数'
    #
    # if match12:
    #     # 使用Match获得分组信息
    #     print match12.group()
    # else:
    #     print u'match12不是小数'
    #
    # if match21:
    #     # 使用Match获得分组信息
    #     print match21.group()
    # else:
    #     print u'match21不是小数'
    #
    # if match22:
    #     # 使用Match获得分组信息
    #     print match22.group()
    # else:
    #     print u'match22不是小数'

    tmp = '<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=2e8f3ca53af33a879e6d0012f65d1018/4ece3bc79f3df8dc2ab63004cd11728b46102899.jpg" width="560" height="400" changedsize="true">'
    print (tmp)


    imgre = re.compile(r'src=(".*\.jpg") width=')
    print (imgre.findall(tmp))



def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    # return imglist

    file = '/home/chenwei/tmp/python_img'
    if not os.path.exists(file):
        print ("创建文件夹",file)
        os.makedirs(file)

    x = 0
    for imgurl in imglist:
        # print x,imgurl
        urllib.urlretrieve(imgurl,file+'/'+'%s.jpg' % x)
        x+=1


def get_version():

    return sys.version

def test_requests():
    pass

    # print(time.time())
    # r = requests.get("https://github.com/timeline.json")
    #
    # # print(r.raw.read(10))
    # #
    # # # print(r.json())
    # print(r.text)
    # print(r.headers)
    # print(r.headers['content-type'])
    # # # print(r.encoding)
    # # # print(r.content)
    # print(time.time())

    # i = Image.open(StringIO(r.content))

    # r = requests.post("http://httpbin.org/post")

    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.get("http://httpbin.org/get", params=payload)
    #
    # print(r.url)
    # print(r.status_code)

    # url = 'https://api.github.com/some/endpoint'
    # payload = {'some': 'data'}
    # headers = {'content-type': 'application/json'}
    #
    # r = requests.post(url, data=json.dumps(payload), headers=headers)
    # print(type(payload))
    # print(type(json.dumps(payload)))
    # print(r.text)

    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.post("http://httpbin.org/post", data=payload)
    # print(r.text)

    # url = 'http://httpbin.org/post'
    # # files = {'file': ('example.log', open('example.log', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
    # files = {'file': ('example.log', 'some,data,to,send\nanother,row,to,send\n')}
    # r = requests.post(url, files=files)
    # print(r.text)

    # r = requests.get('http://httpbin.org/get')
    # print(r.status_code)
    # if r.status_code == requests.codes.ok:
    #     print(True)
    #
    # bad_r = requests.get('http://httpbin.org/status/404')
    # print(bad_r.status_code)
    # if bad_r.status_code == requests.codes.ok:
    #     print(True)
    # else :
    #     print(False)
    #
    # bad_r.raise_for_status()

    # url = 'http://www.saiwei.info'
    # r = requests.get(url)
    # print(r.status_code)
    # print(r.cookies)

    # url = 'http://httpbin.org/cookies'
    # cookies = dict(cookies_are='working')
    # r = requests.get(url, cookies=cookies)
    # print(r.text)

    # r = requests.get('http://github.com')
    # print(type(r))
    # r = requests.get('http://www.saiwei.info',allow_redirects=False)
    # print(r.url)
    # print(r.status_code)
    # print(r.history)

    # s = requests.Session()

    # s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    # r = s.get("http://httpbin.org/cookies")
    #
    # print(r.text)

    # r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
    # print(r.cookies)

    # r = requests.get('https://kennethreitz.com', verify=False)
    # r = requests.get('https://kennethreitz.com')
    # print(r.status_code)

    # hooks=dict(response=print_url)
    # r = requests.get('http://httpbin.org', hooks=dict(response=print_url()))
    # print(r)
    # print_url(r)

# def print_url(r):
#     print(r.url)

def get_session():
    '''
    get requests session, which automatically handles cookies for us
    '''
    v2ex_session = requests.Session()
    user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/32.0.1700.107 Chrome/32.0.1700.107 Safari/537.36"

    header = {'User-Agent': user_agent,
              'Host': 'www.v2ex.com',
              'Origin': 'http://www.v2ex.com',
              'Referer': 'http://www/v2ex.com/signin',
    }
    v2ex_session.headers.update(header)


    return v2ex_session

def main():

    # define urls will be used
    index_url = 'http://v2ex.com'
    sign_url = 'http://v2ex.com/signin'
    mission_url = 'http://v2ex.com/mission/daily'

    # fill in username and password here
    username = 'a6377508'
    password = '6377508'

    # find login needed value 'once', which is hidden in login form
    v2ex_session = get_session()
    # v2ex_session.get(index_url)
    login = v2ex_session.get(sign_url)
    once = re.search(r'value="(\d+)" name="once"', login.text).group(1)
    postdata = {
        'u': username,
        'p': password,
        'once': once,
        'next': '/'
    }

    rsp = v2ex_session.post(sign_url, data=postdata)
    ''':type : requests.Response'''


    if rsp.url[:-1]== sign_url:
        print("登陆失败")
    elif rsp.url[:-1] == index_url:
        print("登陆成功")
    else :
        print(rsp.url)


    # requests.get().history
    # if response.status_code == response.status_code.ok :
    #     pass
    # print(response.text)

    ##<class 'requests.models.Response'>
    ##<class 'requests.models.Response'>
    # print(type(rsp))
    # print(rsp.url)


    # mission_page = v2ex_session.get(mission_url)
    # if "每日登录奖励已领取" in mission_page.text:
    # 	print "每日奖励已领取"
    # 	return
    #
    # # if mission is not done yet, get it
    # mission = re.findall("onclick=.* = '(.*)'", mission_page.content)[0]
    # mission = index_url + mission
    #
    # v2ex_session.get(mission)


def f(param):
    '''
    :type param:int
    :param param:
    :return:
    '''

    param.bit_length()

def test_config():
    pass
    import sys,os
    import configparser
    cf = configparser.ConfigParser()
    cf.read('config.ini')
    # s = cf.sections()
    # print('section:',s)
    # u = cf.options('v2ex')
    # print(u)
    # u = cf.get('v2ex','username')
    # p = cf.get('v2ex','password')
    # print(u+","+p)

    if cf.has_section('v2e'):
        print('has')
    else:
        print('no has')

    u = cf.has_option('v2ex','usernae')
    # u = cf.get('v2ex','usernam')
    print(u)
    item = 'dddd'


    # if not cf.has_section(item):
    #     cf.add_section(item)
    #     cf.set(item,'u1','u2')
    #     cf.write(open("config.ini","w"))
    # else:
    #     cf.set(item,'p1','p2')
    #     cf.write(open("config.ini","w"))
    # if not cf.has_section('dddd'):
    #     cf.add_section('dddd')
    #     cf.set('dddd','u1','u2')
    #     cf.write(open("config.ini","w"))

    # if cf.has_section('dddd'):
    #     cf.remove_section('dddd')
    #     cf.write(open("config.ini","w"))
    # else:
    #     cf.add_section('dddd')
    #     cf.set('dddd','u1','u2')
    #     cf.set('dddd','p1','p2')
    #     cf.write(open("config.ini","w"))
    #
    # cf.set('zhihu','cookies','2222222')
    # cf.write(open("config.ini","w"))



if __name__ == '__main__':
    pass
    # test_requests();
    # main()
    # test_config()

    import requests
    rsp = requests.get('http://www.zhihu.com/login')
    print(rsp.url)


