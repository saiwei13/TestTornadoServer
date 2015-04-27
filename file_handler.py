
# -*- coding: utf-8 -*-
import logging
from os.path import getsize
import tornado

__author__ = 'chenwei'

'''
操作文件的方法
'''

class UploadFileHandler(tornado.web.RequestHandler):
    '''
    上传文件
    '''

    # def post(self, *args, **kwargs):
    #
    #     logging.info("UploadFileHandler  post");
    #
    #     #虽说json其实相当于post的字符串
    #     userinfo_json=self.get_argument('userinfo')
    #     #转化为json对象
    #     userinfo=json.loads(userinfo_json)
    #     parentid_txt=userinfo.get('parentid')
    #     childid_txt=userinfo.get('childid')
    #     #存放为当前路径下的uploadfiles文件夹
    #     upload_path=os.path.join(os.path.dirname(__file__),'uploadfiles')  #文件的暂存路径
    #     file_metas=self.request.files['uploadfile']    #提取表单中‘name’为‘file’的文件元数据
    #     meta=file_metas[0]
    #     #filename=meta['filename']
    #     #获取当前用户已经有过多少张照片，用于上传时的文件名的重命名。
    #     pic_num=utils.getPictureNumber(childid_txt,parentid_txt)
    #     #图片重命名
    #     filename=childid_txt+str(pic_num)+'.'+meta['filename'].split(".")[1]
    #     print(filename)
    #     filepath=os.path.join(upload_path,filename)
    #     with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
    #         up.write(meta['body'])
    #     self.write('finished!')

    def post(self, *args, **kwargs):
        print "post() upload"
        logging.info("post() logging upload")
        fileinfo = self.request.files['myFile'][0]
        print "fileinfo is", fileinfo

        # files = self.request.files
        # print "files is", files

        # fileinfo2 = self.request.get_argument('myFile')
        # print "fileinfo2 is", fileinfo2

        with open("/home/chenwei/tmp/python_server.txt", 'wb') as out:
            # body = self.request.get_argument('data')
            # body = self.request.files['myFile'][0]

            # out.write(bytes(fileinfo['body'], 'utf8'))
            # out.write(fileinfo['filename'],'w')
            out.write(fileinfo['body'])    #验证成功

            # out.write(bytes(fileinfo['body'], 'utf-8'))

        self.finish();
        print 'finish !!!!###'




class DownloadFileHandler(tornado.web.RequestHandler):
    '''
    下载文件
    '''

    # def get(self, filename):
    #     print('get() i download file handler : ',filename)

    def post(self):
        print('post() i download file handler : ')

        filename = "/home/chenwei/tmp/python_server.txt";
        size = 0L;
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
        print 'finish';
