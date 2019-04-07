from sqlalchemy import Column, String, create_engine, BIGINT, Integer, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship, sessionmaker
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


class Person(Base):
    __tablename__ = "p_person"

    p_id = Column("p_id", BIGINT, primary_key=True)

    name = Column("name", String(20), nullable=False)

    address_id = Column("address_id", BIGINT, ForeignKey("p_address.id"))

    """
        relationship:在真正使用该类型定义的字段时进行关系数据获取
        第一个参数为持久类型模型类名，
        back_populates：指定关联类中对应的属性名，该属性必须存在
        backref:指定关联类中对应的属性名,概属性可以不存在，sqlAlchemy会自动生成
        secondary：在多对多关系中该属性用于指定中间表
        cascade:级联。默认为save-update,merge。使用逗号分隔多个。
                    可用级联（save-update、merge、expunge、delete、delete-orphan、refresh-expire）
                    也可使用 all 表示（save-update, merge, refresh-expire, expunge, delete）的简写
    """
    address = relationship("Address", back_populates="persons", lazy="select")


class Address(Base):
    __tablename__ = "p_address"

    id = Column(BIGINT, primary_key=True)

    address_name = Column("address_name", String(20), nullable=False)

    persons = relationship("Person")


# address = Address()
# bases__ = address.__class__.__bases__
# i = filter(lambda base_obj: isinstance(base_obj, DeclarativeMeta), bases__)
# print(list(i))
# print(not list(i))
# print(not address)

a = [1]
if a:
    print("true")
else:
    print("false")
