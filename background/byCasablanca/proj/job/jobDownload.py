from datetime import datetime
import time
import os

# from pymongo import MongoClient

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
# from apscheduler.jobstores.mongodb import MongoDBJobStore

from conf.setting import MONGO_COLLECTION, MONGO_DB, MONGO_HOST, MONGO_PORT

# 自己的package
from common.enum import Area, ProductType
from conf import setting
from model.middlemodel import ProductMidModel, AreaNameMidModel
from core.ftp import Ftp, ProductFile

# 由于 server03 不好安装mongo，且只能安装对应版本为2.0.1 的mongo，暂时修改为 mysql 的方式存储
# client = MongoClient(MONGO_HOST, MONGO_PORT)

job_stores = {
    # 'mongo': MongoDBJobStore(collection=MONGO_COLLECTION, database=MONGO_DB, client=client),
    'default': MemoryJobStore()
}

sched = BlockingScheduler(jobstores=job_stores)


def start():
    sched.start()
    # pass


# @sched.scheduled_job('interval', id='my_product_id', seconds=5)
# @sched.scheduled_job('cron', id='my_product_id', hour=9, minute=0, jobstore='mongo')
@sched.scheduled_job('cron', id='my_product_id', hour=9, minute=48, jobstore='default')
def product_job():
    # todo:[*] 19-10-31 main中的product相关方法放置此处
    # TODO:[-] 20-08-31 py3.4 不支持此种写法，注释掉
    # print(f'执行每日定时任务! The time is: {datetime.now()}')
    print('执行每日定时任务! The time is: '+datetime.now())
    list_products = init_type()
    ftp = Ftp(setting._FTP_HOST, setting._FTP_USER, setting._FTP_PASSWORD)
    product = ProductFile(ftp)
    product.run(list_products)


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
    # todo:[-] 19-12-12 current中不包含FAREAST
    list.append(ProductMidModel(ProductType.CURRENT,
                                [AreaNameMidModel(Area.EASTCHINASEA, 'sped-top*.jpg'),
                                 AreaNameMidModel(Area.NORTHWEST, '048_UV*.png'),
                                 AreaNameMidModel(Area.FAREAST, 'cur_NMEFC_near_goos_*.png')],
                                os.path.join(setting._ROOT_DIR, 'current')))
    # list.append(ProductMidModel(ProductType.CURRENT,
    #                             [AreaNameMidModel(Area.EASTCHINASEA, 'sped-top*.jpg'),
    #                              AreaNameMidModel(Area.NORTHWEST, '048_UV*.png')],
    #                             os.path.join(setting._ROOT_DIR, 'current')))
    # todo:[-] 19-10-30 注意海冰的命名方式有一些特殊，注意
    # todo:[*] 19-12-12 注意所有海冰相关的暂时注释掉
    # list.append(ProductMidModel(ProductType.ICE,
    #                             [AreaNameMidModel(Area.BOHAI, '19*.jpg')],
    #                             os.path.join(setting._ROOT_DIR, 'ice')))

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
