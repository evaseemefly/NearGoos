import sys
import os

# 自己的package
from common.enum import Area, ProductType
from conf import setting
from model.middlemodel import ProductMidModel, AreaNameMidModel
from core.ftp import Ftp

cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)


def main():
    list_products = init_type()
    ftp = Ftp(setting._FTP_HOST, setting._FTP_USER, setting._FTP_PASSWORD)
    ftp.init_ftp()
    # ftp.copy_list(list_products)
    ftp.run(list_products)
    pass


def init_type() -> []:
    '''
        初始化product type
    :return:
    '''
    list = []
    list.append(ProductMidModel(ProductType.WAVE,
                                [AreaNameMidModel(Area.CHINASEA, 'coast*.png'),
                                 AreaNameMidModel(Area.NORTHWEST, 'xb*.png')],
                                os.path.join(setting._ROOT_DIR,'wave')))
    return list


def get_type_dict():
    '''
        获取字典中的匹配正则
    :return:
    '''

    pass


if __name__ == '__main__':
    main()
