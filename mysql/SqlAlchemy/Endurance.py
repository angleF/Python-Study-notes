from sqlalchemy import Column, String, create_engine, BIGINT, Integer, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

# 创建对象的基类
Base = declarative_base()


# 定义持久化类
# 继承declarative_base()基类，SqlAlchemy将默认实现__init__函数,
# 并且将所有映射的字段放入形参中并进行赋值
class Statistics(Base):
    # 表名 必须定义
    __tablename__ = 'statistics'

    # 主键
    id = Column(Integer, primary_key=True)

    im_uid = Column(name="im_uid", type_=String(100))

    effective_advisory = Column(name="effective_advisory", type_=Integer)

    first_avg_reply = Column("first_avg_reply", Integer)

    avg_reply = Column(name="avg_reply", type_=Integer)

    first_reply_session_id = Column(name="first_reply_session_id", type_=String(2000))

    operating_data_time = Column("operating_data_time", Date)

    create_user = Column("create_user", String(50))

    create_time = Column("create_time", DateTime, default=datetime.datetime.now)

    update_user = Column(name="update_user", type_=String(50))

    update_time = Column(name="update_time", type_=DateTime)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}