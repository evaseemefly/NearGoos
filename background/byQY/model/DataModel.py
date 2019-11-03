# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class DataArea(Base):
    __tablename__ = 'data_area'

    id = Column(BIGINT(20), primary_key=True, index=True)
    gmt_create = Column(DateTime, nullable=False)
    gmt_modified = Column(DateTime, nullable=False)
    is_delete = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    name = Column(String(20), nullable=False)


class DataCategory(Base):
    __tablename__ = 'data_category'

    id = Column(BIGINT(20), primary_key=True, index=True, autoincrement=True)
    gmt_create = Column(DateTime, nullable=False)
    gmt_modified = Column(DateTime, nullable=False)
    is_delete = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    name = Column(String(50), nullable=False)
    remark = Column(String(50))


class DataSource(Base):
    __tablename__ = 'data_source'

    id = Column(BIGINT(20), primary_key=True, index=True)
    gmt_create = Column(DateTime, nullable=False)
    gmt_modified = Column(DateTime, nullable=False)
    is_delete = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    img_url = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False)
    homepage_url = Column(String(100))


class DataDataInfo(Base):
    __tablename__ = 'data_data_info'

    id = Column(BIGINT(20), primary_key=True)
    gmt_create = Column(DateTime, nullable=False)
    gmt_modified = Column(DateTime, nullable=False)
    is_delete = Column(TINYINT(4), nullable=False)
    name = Column(String(100), nullable=False)
    extensions = Column(String(10), comment='扩展名')
    remark = Column(String(100))
    date = Column(DateTime, nullable=False, comment='数据观测日期')
    is_desc = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    category_id = Column(ForeignKey('data_category.id', onupdate='CASCADE'), index=True)
    source_id = Column(ForeignKey('data_source.id', onupdate='CASCADE'), index=True)
    area_id = Column(ForeignKey('data_area.id', onupdate='CASCADE'), index=True)
    url = Column(String(100), nullable=False)
    date_ftp = Column(DateTime)
    size = Column(BIGINT(20))
    location = Column(String(10))

    area = relationship('DataArea')
    category = relationship('DataCategory')
    source = relationship('DataSource')
