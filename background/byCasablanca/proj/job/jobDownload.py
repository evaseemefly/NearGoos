from datetime import datetime
import time
import os

from pymongo import MongoClient

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.mongodb import MongoDBJobStore

from conf.setting import MONGO_COLLECTION, MONGO_DB, MONGO_HOST, MONGO_PORT

client = MongoClient(MONGO_HOST, MONGO_PORT)

job_stores = {
    'mongo': MongoDBJobStore(collection=MONGO_COLLECTION, database=MONGO_DB, client=client),
    'default': MemoryJobStore()
}

sched = BlockingScheduler(jobstores=job_stores)


def start():
    sched.start()
    # pass


# @sched.scheduled_job('interval', id='my_product_id', seconds=5)
@sched.scheduled_job('cron', id='my_product_id', hour=16, minute=16, jobstore='mongo')
def product_job():
    # todo:[*] 19-10-31 main中的product相关方法放置此处
    print('Tick! The time is: %s' % datetime.now())
