import configparser
from datetime import datetime,date
import random
import requests
from mock_login.base_client import BaseClient

__author__ = 'chenwei'


##判断是否登陆

class Renren(BaseClient):
    def __init__(self,email,password):

        self.email = email
        self.password = password
        self.session = requests.session()

        self.index_url = 'http://www.renren.com/'
        self.sign_url = 'http://www.zhihu.com/login'
        self.encryptkey_url = 'http://login.renren.com/ajax/getEncryptKey'

        self.config_section = 'renren'
        '''配置文件字段'''
        self.config_cookies = 'cookies'
        '''配置文件字段'''

        print('email = %s , pwd=%s' %(email,password))

    def sign_in(self):
        pass

        self.load_cookies()

        # rsp = self.session.get(self.index_url)
        # # if '".*/login.js"' in rsp.text:
        # # if 'login.js' in rsp.text:      ##注意
        # # if '"login.js"' in rsp.text:
        #     print("未登陆")
        # else:
        #     print("已登陆")
        #
        # print(rsp.text)
        # print("跳转url=",rsp.url)

        # return
        from mock_login import rsa

        key = self.getEncryptKey()
        print(key)

        header = {
            'Accept': '*/*',
            'Origin': 'http://www.renren.com',
            'X-Requested-With': "XMLHttpRequest",
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': "http://www.renren.com/",
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4'
        }

        post_data={
                'captcha_type': 'web_login',
                'domain': 'renren.com',
                'email': self.email,
                'key_id': '1',
                'origURL': 'http://www.renren.com/home',

                'password':rsa.encryptString(key['e'],key['n'],self.password),
                'rkey':key['rkey'],

                # 'password': '2f4d738df681b2b461a11d9aecb1c75bbdea9a60cef42bb2711e585b40973b27',
                # 'rkey':'c5c08b36d1daef7b10b7ae3c886850e6',

                # 'password': '1b939a7fe518ac8ba13bb3cb86cd75b63f57f672b3f9af6c7eafcd4fa3a11ab1',
                # 'rkey':'2def5d84381e7889d5a3035d83561d72',

                # 'password': '28bcdc779d96730b57a860db7165053c83b97e713927a48d7c76203af35806ec',
                # 'rkey':'d5921c94a281db272ce6560db2f03780',
        }

        # 18ae8d66e33b8d92da61d7150053509b4a0cc4e6bfafdf3fa117efdd72e6b7f8

        # url = self.get_url();
        # print('url=',url);
        #
        url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=%f' % random.random()

        rsp = self.session.post(
            # url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2015452210746',
            url=url,
            data=post_data,
            headers=header,
        )
        ''':type : requests.Response'''
        print(rsp.status_code)
        print(rsp.json())
        if rsp.status_code == 200:
            if rsp.json()['code']:
                self.save_cookies();
        else:
            print(rsp.status_code)



    def getEncryptKey(self):
        print('getEncryptKey()')
        r = requests.get(self.encryptkey_url)
        ''':type r : requests.Response'''
        print (r.status_code)
        return r.json()

    def get_url(self):
        # http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2015452252190
        now = datetime.now()
        year = now.year
        month = now.month-1
        day = now.weekday()+1
        if day == 7:
            day = 0;
        hour = now.hour
        second = now.second
        millsecond = round(now.microsecond/1000)

        url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=%d%d%d%d%d%d" % (year,month,day,hour,second,millsecond);
        return url

if __name__ == '__main__':


    from mock_login.util import config_file

    cf = configparser.ConfigParser()
    cf.read(config_file)

    renren = Renren(
        email=cf.get('renren','email'),
        password=cf.get('renren','password')
    )
    renren.sign_in();
    # renren.test();

