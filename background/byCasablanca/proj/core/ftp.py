from ftplib import FTP, FTP_TLS
from ftplib import error_perm
import os
from fnmatch import fnmatch, fnmatchcase
import socket

# 中间mid model
from model.middlemodel import ProductMidModel, AreaNameMidModel
# 自定义工具
from common import tools


class Ftp():
    ftp = None

    def __init__(self, host, user, pwd, port=21):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port

    def init_ftp(self):
        '''
            初始化ftp
        :return:
        '''
        if self.ftp is None:
            self.ftp = FTP()
            if all([self.host, self.user, self.pwd]):
                # todo:[-] 19-10-29 加入连接错误以及用户名及密码错误的异常处理
                # 参考
                try:

                    self.ftp.set_debuglevel(0)
                    self.ftp.connect(self.host, self.port)
                    self.ftp.login(self.user, self.pwd)
                    print(self.ftp.getwelcome())
                    # msg=self.ftp.retrlines('LIST xb*')
                except(socket.error, socket.gaierror):
                    print(f"连接错误:{self.host, self.port}")
                    self.ftp = None
                except error_perm:
                    # 认证错误
                    print("认证错误，请检查用户名及密码")
                    self.ftp = None

    def run(self, list):
        '''
            ftp的执行方法(入口方法)
        :return:
        '''
        self._copy_list(list)

    def download_file(self, file_name: str, local_path: str):
        '''
            将ftp目录下的指定文件下载至本地的指定目录下
        :param remote_path:
        :param local_path:
        :return:
        '''
        cache_size = 1024
        # todo:[*] 19-10-29 此处需要判断本地路径是否存在
        # 将此方法统一放在common.tools中
        tools.check_path_exist(local_path)
        fp = open(os.path.join(local_path, file_name), 'wb')
        # 读取指定文件并写入本地文件
        # 错误1:ftplib.error_perm: 500 Syntax error, command unrecognized.
        msg = self.ftp.retrbinary('RETR ' + file_name, fp.write, cache_size)
        # 判断ftp返回的状态
        if msg.find('226') != -1:
            print("下载完毕")
            # todo:[*] 19-10-29 以后需要改造为写入数据库操作
        self.ftp.set_debuglevel(0)
        fp.close()

        pass

    def _copy_list(self, list: []):
        '''

        :param list:
        :return:
        '''
        for product in list:
            if isinstance(product, ProductMidModel):
                for area_temp in product.areanames:
                    # 根据区域的re找到ftp中符合条件的file list
                    list_match_files = self._get_match_list(area_temp.re)
                    # 对符合条件的 file list 进行遍历
                    # -1 [-] 获取要存储的目录
                    # -2 [-] 下载并存储至指定目录
                    # -3 [*] 记录最终的目录并写入数据库
                    # -4 [*] 清除ftp上的相应的文件
                    for file_temp in list_match_files:
                        print(file_temp)
                        self.download_file(file_temp, product.root)

        # pass

    def _get_match_list(self, re_str: str) -> []:
        '''
            获取匹配条件的list
        :param model:
        :return:
        '''
        list_names = self.ftp.nlst()
        list_match = [name for name in list_names if fnmatch(name, re_str)]
        return list_match

# def get_match_list()
