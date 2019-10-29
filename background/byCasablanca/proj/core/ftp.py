from ftplib import FTP, FTP_TLS
import re
from fnmatch import fnmatch, fnmatchcase

from model.middlemodel import ProductMidModel, AreaNameMidModel


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
                self.ftp.set_debuglevel(0)
                self.ftp.connect(self.host, self.port)
                self.ftp.login(self.user, self.pwd)
                print(self.ftp.getwelcome())
                # msg=self.ftp.retrlines('LIST xb*')

    def run(self, list):
        '''
            ftp的执行方法
        :return:
        '''
        self._copy_list(list)

    def download_file(self,remote_path:str,local_path:str):
        '''
            将ftp目录下的指定文件下载至本地的指定目录下
        :param remote_path:
        :param local_path:
        :return:
        '''
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
                    # -1 获取要存储的目录
                    # -2 下载并存储至指定目录
                    # -3 记录最终的目录并写入数据库
                    # -4 清除ftp上的相应的文件
                    for file_temp in list_match_files:
                        print(file_temp)

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
