from sqlalchemy import Column, String, create_engine, BIGINT, Integer, Date, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from JsonEncode import to_json_str
from mysql.MyLog import logger
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


if __name__ == "__main__":
    #     初始化数据库连接 echo=True :使用Python标准logging模块打印sql
    # SqlAlchemy使用懒连接，只有在真正操作数据库时才创建连接
    sql_engine = create_engine("mysql://root:123456@localhost/test?charset=utf8", echo=True)
    # 创建Base对象所有子类对象映射表（数据库中该表名不存在则创建）
    Base.metadata.create_all(sql_engine)
    # sessionmaker类相当于一个session工厂，用于创建session
    session_instance = sessionmaker(bind=sql_engine)
    session = session_instance()

    # 查询满足条件的第一条数据
    query = session.query(Statistics)
    first_statistics = query.filter_by(im_uid='S_2').first()
    logger.info("im_uid=2第一条数据：%s", to_json_str(first_statistics))
    # 查询主键等于1
    primaryKey_result = query.get(1)
    logger.info("主键=1：%s", to_json_str(primaryKey_result))

    # 只查询create_user和update_user字段，该方式返回集合，集合中元素为元组，元组包含指定查询字段的值
    # 返回格式示例：[('system', 'system'), ('system', 'system')]
    session_query = session.query(Statistics.id, Statistics.create_user, Statistics.update_user). \
        order_by(Statistics.id).all()
    logger.info(session_query)

    # 查询过滤
    # query中只有一个字段时返回二维列表
    # 返回示例：[[4], [5], [6], [8], [10], [11], [12], [13], [14], [15], [16], [17], [18]]
    id_query = session.query(Statistics.id)

    # 查询id大于3 >
    id_filter_all = id_query.filter(Statistics.id > 3).all()
    logger.info("id大于3：%s", to_json_str(id_filter_all))

    # 查询first_avg_reply不等于3000的所有id !=
    reply_not_all = id_query.filter(Statistics.first_avg_reply != 3000).all()
    logger.info("first_avg_reply不等于3000的所有id：%s", to_json_str(reply_not_all))

    # 查询first_reply_session_id为sd开头的所有id like
    before_like_all = id_query.filter(Statistics.first_reply_session_id.like('sd%')).all()
    logger.info("first_reply_session_id为sd开头的所有id：%s", to_json_str(before_like_all))

    # 查询first_reply_session_id为Sd(不区分大小写)开头的所有id
    before_ilike_all = id_query.filter(Statistics.first_reply_session_id.ilike('Sd%')).all()
    logger.info("first_reply_session_id为Sd(不区分大小写)开头的所有id：%s", to_json_str(before_ilike_all))

    # 查询avg_reply为100, 200, 300的所有id in
    in_avg_reply_all = id_query.filter(Statistics.avg_reply.in_([100, 200, 300])).all()
    logger.info("avg_reply为100, 200, 300的所有id：%s", to_json_str(in_avg_reply_all))

    # 查询avg_reply不为100, 200, 300的所有id not in 关键符号 ~
    not_in_avg_reply_all = id_query.filter(~Statistics.avg_reply.in_([100, 200, 300])).all()
    logger.info("avg_reply不为100, 200, 300的所有id：%s", to_json_str(not_in_avg_reply_all))

    # IS NULL
    none__all = id_query.filter(Statistics.avg_reply == None).all()
    logger.info("avg_reply为null的所有id(==)：%s", to_json_str(none__all))

    # IS NULL is_(None)和==None 生成的sql都是一致的，即条件为：IS NULL
    in__none__all = id_query.filter(Statistics.avg_reply.is_(None)).all()
    logger.info("avg_reply为null的所有id(is)：%s", to_json_str(in__none__all))

    # AND 有多种方式
    from sqlalchemy import and_
    id_and_package_all = id_query.filter(
        and_(Statistics.avg_reply.is_(None), Statistics.first_avg_reply != None)).all()
    logger.info("使用and_函数：%s", to_json_str(id_and_package_all))
    # AND 直接使用逗号,不需要额外导包
    id_and_all = id_query.filter(Statistics.avg_reply.is_(None), Statistics.first_avg_reply != None).all()
    logger.info("直接使用逗号(不需要额外导包)：%s", to_json_str(id_and_all))
    # AND 使用filter方法链,不需要额外导包
    id_and_all = id_query.filter(Statistics.avg_reply.is_(None)).filter(Statistics.first_avg_reply != None).all()
    logger.info("使用filter方法链(不需要额外导包)：%s", to_json_str(id_and_all))

    # OR 需要导包
    from sqlalchemy import or_
    id_or_all = id_query.filter(
        or_(Statistics.avg_reply.is_(None), Statistics.first_avg_reply != None)).all()
    logger.info("OR 需要导包：%s", to_json_str(id_or_all))

    # one() 使用one函数如查询到结果为空或者大于1条都会报错
    id__one = id_query.filter(Statistics.id == 2).one()
    logger.info("使用one函数查询id=2：%s", to_json_str(id__one))

    # first() 限制值查询一条与one区别在于 会在sql语句中限制查询条数，所以，要么一条要么没有（在mysql中使用limit 1）
    id_first_all = id_query.filter(Statistics.avg_reply.is_(None)).filter(Statistics.first_avg_reply != None).first()
    logger.info("使用first限制查询一条：%s", to_json_str(id_first_all))

    # one_or_none()和scalar() 这两个函数都和one函数有类似的地方
    # one_or_none返回空不会报错，但是返回多条会报错
    # scalar()目前发现和one一致

    # 设置每次事务自动提交，确认为False
    # session.autocommit = True
    # 添加
    # statistics = Statistics()
    # statistics.avg_reply = 200
    # statistics.create_user = "system"
    # statistics.effective_advisory = 1024
    # statistics.first_avg_reply = 3000
    # statistics.first_reply_session_id = "sdsdsadsaasdasdasdsadvzxcvzxasdsa"
    # statistics.im_uid = "S_11"
    # statistics.operating_data_time = datetime.date.today()
    # statistics.update_time = datetime.datetime.now()
    # statistics.update_user = "system"
    # session.add(statistics)
    # # session.commit()
    # logger.info("添加成功后的主键：%s", statistics.id)
    # # 批量添加
    # session.add_all([Statistics(im_uid="S_12"), Statistics(im_uid="S_13")
    #                     , Statistics(im_uid="S_14")])
    # statistics.first_reply_session_id = '88888888'
    #
    # # 回滚
    # # session.rollback()
    # session.commit()
