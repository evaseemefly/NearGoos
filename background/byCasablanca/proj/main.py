import sys
import os
from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler
# 自己的package
from common.enum import Area, ProductType
from conf import setting
from model.middlemodel import ProductMidModel, AreaNameMidModel
from core.ftp import Ftp, ProductFile
# 引入自定义的job
from job.jobDownload import tick,start

cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)


def main():
    # todo:[*] 19-10-31 引入定时任务 以下暂时注释掉
    # list_products = init_type()
    # ftp = Ftp(setting._FTP_HOST, setting._FTP_USER, setting._FTP_PASSWORD)
    # product = ProductFile(ftp)
    # product.run(list_products)

    # 方式1：
    # scheduler = BlockingScheduler()
    # scheduler.add_job(tick, 'interval', seconds=3)
    # scheduler.start()
    start()
    # 方式2：

    print('定时任务启动')
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
                                os.path.join(setting._ROOT_DIR, 'wave')))
    list.append(ProductMidModel(ProductType.CURRENT,
                                [AreaNameMidModel(Area.EASTCHINASEA, 'sped-top*.jpg'),
                                 AreaNameMidModel(Area.NORTHWEST, '048_UV*.png'),
                                 AreaNameMidModel(Area.FAREAST, 'cur_NMEFC_near_goos_*.png')],
                                os.path.join(setting._ROOT_DIR, 'current')))
    # todo:[-] 19-10-30 注意海冰的命名方式有一些特殊，注意
    list.append(ProductMidModel(ProductType.ICE,
                                [AreaNameMidModel(Area.BOHAI, '19*.jpg')],
                                os.path.join(setting._ROOT_DIR, 'ice')))

    list.append(ProductMidModel(ProductType.SST,
                                [AreaNameMidModel(Area.EASTCHINASEA, 'temp-top-*.jpg'),
                                 AreaNameMidModel(Area.NORTHWEST, '024_T_*.png')],
                                os.path.join(setting._ROOT_DIR, 'SST')))
    list.append(ProductMidModel(ProductType.SSH,
                                [AreaNameMidModel(Area.FAREAST, 'ssh_NMEFC_near_goos_*.png')],
                                os.path.join(setting._ROOT_DIR, 'SSH')))
    return list


def get_type_dict():
    '''
        获取字典中的匹配正则
    :return:
    '''

    pass


if __name__ == '__main__':
    main()