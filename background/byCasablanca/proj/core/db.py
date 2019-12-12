from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from model.models import ProductInfoModel, Base
from conf import setting


class DBFactory:
    session: sessionmaker = None

    def __init__(self):
        self.host = setting.DB_HOST
        self.port = setting.DB_PORT
        self.user = setting.DB_USER
        self.pwd = setting.DB_PWD
        self.db_name = setting.DB_NAME
        # self.engine_str = f'mysql+mysqlconnector://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.db_name}'
        # TODO:[-] 19-12-12 ModuleNotFoundError: No module named 'mysql' 切换 mysqlconnector->mysqldb
        self.engine_str = f'mysql+mysqldb://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.db_name}'

        pass

    def _init_session(self):
        if self.session is None:
            engine = create_engine(self.engine_str, echo=True, encoding='utf-8')
            Base.metadata.create_all(engine)
            self.session = sessionmaker(bind=engine)
            return self.session
        else:
            return None

    def insert_to_db(self, **kwargs):
        if self.session is None:
            self._init_session()
        session = self.session()
        product = ProductInfoModel(name=kwargs.get('name'),
                                   area=kwargs.get('area').value,
                                   interval=int(kwargs.get('interval')),
                                   image_url=kwargs.get('image_url'),
                                   target_date=kwargs.get('target_date'),
                                   gmt_create=kwargs.get('create'),
                                   gmt_modified=kwargs.get('modified'),
                                   type=kwargs.get('type').value,
                                   file_name=kwargs.get('file_name'),
                                   relative_path=kwargs.get('relative_path'),
                                   root_path=kwargs.get('root_path'),
                                   ext=kwargs.get('ext'))
        # todo:[-] 19-10-30 错误：
        # 'sessionmaker' object has no attribute 'add'
        # 注意sessionmaker创建的，需要实例化！
        session.add(product)
        session.commit()

    def commit(self):
        session = self.session()
        session.commit()
