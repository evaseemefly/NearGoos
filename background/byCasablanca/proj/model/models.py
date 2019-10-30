import datetime

from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductInfoModel(Base):
    '''
        对应数据库的 product info 表
        用来存储产品图片以及相关信息

    '''
    __tablename__ = 'product_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    area = Column(Integer)
    interval = Column(Integer)
    image_url = Column(String)
    target_date = Column(DateTime)
    gmt_create = Column(DateTime, default=datetime.datetime.utcnow())
    gmt_modified = Column(DateTime, default=datetime.datetime.utcnow())
    type = Column(Integer)
