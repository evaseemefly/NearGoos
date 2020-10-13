from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from model.models import ProductInfoModel, Base
from conf import setting


class DBFactory:
    # TODO:[-] 20-08-31 py3.4 不支持此种写法，注释掉
    # session: sessionmaker = None
    session = None

    def __init__(self):
        self.host = setting.DB_HOST
        self.port = setting.DB_PORT
        self.user = setting.DB_USER
        self.pwd = setting.DB_PWD
        self.db_name = setting.DB_NAME
        # self.engine_str = f'mysql+mysqlconnector://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.db_name}'
        # TODO:[-] 19-12-12 ModuleNotFoundError: No module named 'mysql' 切换 mysqlconnector->mysqldb
        # TODO:[-] 20-08-31 py3.4 不支持此种写法，注释掉
        # self.engine_str = f'mysql+mysqldb://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.db_name}'
        # 'mysql+mysqldb://root:123456@localhost:3306/neargoos'
        # 注意此处修改 为 pymysql 之前为 [mysqldb]
        # 使用 mysqldb 还是会报错，切换为 mysqlconnector 之前为 [pymysql]
        # conda install -c conda-forge mysql-connector-python
        # TODO:[-] 20-10-13 数据库连接引擎由于py版本的问题，使用的引擎不同
        # 在本地测试时 连接引擎 暂时修改为 mysqldb 实际线上使用 [x] mysqlconnector| [-] pymysql
        # 本地测试使用 mysqldb mysal8.0 py3.7
        # 线上使用 pymysql  mysql5.6 py3.4
        self.engine_str = 'mysql+pymysql://' + self.user + ':' + self.pwd + '@' + self.host + ':' + str(
            self.port) + '/' + self.db_name
        pass

    def _init_session(self):
        if self.session is None:
            # TODO:[*] 20-10-13 py3.4 出现以下错误
            # ImportError: No module named 'MySQLdb'
            # 数据库连接引擎修改为 pymysql 之前为 [mysqldb]
            engine = create_engine(self.engine_str, echo=True, encoding='utf-8')
            # TODO:[*] 20-10-13 此处会报错 KeyError: 255 暂时注释掉
            # Base.metadata.create_all(engine)
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
        # TODO:[*] 20-10-13 提交时出错
        # error1: 替换为 pymysql 时出错
        # sqlalchemy.util.queue.Empty
        # During handling of the above exception, another exception occurred:
        # error2: 替换为 mysqlconnector 时出错
        # sqlalchemy.exc.DatabaseError: (mysql.connector.errors.DatabaseError) 1193 (HY000): Unknown system variable 'tx_isolation'
        # -> mysql.connector.errors.DatabaseError: 1193 (HY000): Unknown system variable 'tx_isolation'
        # mysql 5.6 及以前版本 用的是tx_isolation
        # mysql8，现在更名为 transaction_isolation
        # 而 mysql-connection 对于 5.7 以后的版本没有支持
        # 目前在本地测试时由于使用的 mysql8.0 暂时修改为 mysqldb
        session.commit()
        pass

    def commit(self):
        session = self.session()
        session.commit()
