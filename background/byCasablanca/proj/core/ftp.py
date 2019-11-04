from ftplib import FTP, FTP_TLS
from ftplib import error_perm
import os
from fnmatch import fnmatch, fnmatchcase
import socket
from datetime import date, datetime

# 中间mid model
from model.middlemodel import ProductMidModel, AreaNameMidModel
from model.models import ProductInfoModel
# 自定义工具
from common import tools
from core.db import DBFactory


class Ftp:
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
                except Exception as e:
                    print(f"其他未知错误{e}")
                    self.ftp = None

    # todo:[-] 19-10-30 放在product file中
    # def run(self, list):
    #     '''
    #         ftp的执行方法(入口方法)
    #     :return:
    #     '''
    #     self._copy_list(list)

    def download_file(self, file_name: str, local_path: str):
        '''
            将ftp目录下的指定文件下载至本地的指定目录下
        :param remote_path:
        :param local_path:
        :return:
        '''
        cache_size = 1024
        # todo:[-] 19-10-29 此处需要判断本地路径是否存在
        # 将此方法统一放在common.tools中
        tools.check_path_exist(local_path)
        fp = open(os.path.join(local_path, file_name), 'wb')
        # 读取指定文件并写入本地文件
        # 错误1:ftplib.error_perm: 500 Syntax error, command unrecognized.
        msg = self.ftp.retrbinary('RETR ' + file_name, fp.write, cache_size)
        # 判断ftp返回的状态
        if msg.find('226') != -1:
            print("下载完毕")
            # todo:[-] 19-10-29 以后需要改造为写入数据库操作:放在下载之后，已完成
        self.ftp.set_debuglevel(0)
        fp.close()

        pass

    def delete_file(self, file_name: str, remote_path: ''):
        '''
            删除远端的file
        :param file_name:
        :param remote_path:
        :return:
        '''
        if remote_path == '':
            self.ftp.delete_file(file_name)

    #
    # todo:[-] 19-10-30 放在product file中
    # def _copy_list(self, list: []):
    #     '''
    #
    #     :param list:
    #     :return:
    #     '''
    #     for product in list:
    #         if isinstance(product, ProductMidModel):
    #             for area_temp in product.areanames:
    #                 # 根据区域的re找到ftp中符合条件的file list
    #                 list_match_files = self._get_match_list(area_temp.re)
    #                 # 对符合条件的 file list 进行遍历
    #                 # -1 [-] 获取要存储的目录
    #                 # -2 [-] 下载并存储至指定目录
    #                 # -3 [*] 记录最终的目录并写入数据库
    #                 # -4 [*] 清除ftp上的相应的文件
    #                 for file_temp in list_match_files:
    #                     print(file_temp)
    #                     self.download_file(file_temp, product.root)
    #
    #     # pass

    def get_all_list(self) -> []:
        return self.ftp.nlst()


# def get_match_list()
class ProductFile:
    session = None

    def __init__(self, ftp: Ftp):
        self.ftp = ftp

    def run(self, list: []):
        self.ftp.init_ftp()
        self.copy_list(list)

    def copy_list(self, list: []):
        '''
            根据产品种类找到符合条件的文件并复制到本地指定目录
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
                    # -4 [-] 清除ftp上的相应的文件
                    db = DBFactory()
                    for file_temp in list_match_files:
                        print(file_temp)
                        # todo:[-] 19-10-30 此处的下载的地址，需要加入时间（只根据product的type进行分类:wave|current|ice/ssh/sst，不再产品中再对区域进行细分了）
                        # 此处加一个时间的目录结构
                        now_date = date.today()
                        root_path = product.root
                        relative_path = os.path.join(str(now_date.year), str(now_date.month),
                                                     str(now_date.day))
                        final_path = os.path.join(root_path, relative_path)
                        self.ftp.download_file(file_temp, final_path)
                        # todo:[*] 19-10-30 加入写入数据库的操作，此处暂时先这样实现，需要改为工厂模式
                        # db = DBFactory()
                        # todo:[*] 19-10-31 此处的interval未完成——此处可以暂时不写间隔
                        db.insert_to_db(name=file_temp,
                                        area=area_temp.area,
                                        interval=0,
                                        image_url=final_path,
                                        target_date=datetime.utcnow(),
                                        type=product.producttype,
                                        root_path=root_path,
                                        relative_path=relative_path,
                                        file_name=file_temp)

                        # todo:[*] 19-10-30 暂时不执行ftp删除操作，暂时注释掉
                        # self.ftp.delete_file(file_temp)
                    # db.commit()
        # pass
        pass

    def _get_match_list(self, re_str: str) -> []:
        '''
            获取匹配条件的list
        :param model:
        :return:
        '''
        list_names = self.ftp.get_all_list()
        list_match = [name for name in list_names if fnmatch(name, re_str)]
        return list_match

    def _insert_to_db(self, **kwargs):
        product = ProductInfoModel(name=kwargs.get('name'), area=kwargs.get('area'),
                                   interval=int(kwargs.get('interval')), image_url=kwargs.get('image_url'),
                                   target_date=kwargs.get('target_date'), gmt_create=kwargs.get('create'),
                                   gmt_modified=kwargs.get('modified'), type=kwargs.get('type'))
