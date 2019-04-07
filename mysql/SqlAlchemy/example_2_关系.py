from mysql.SqlAlchemy.Endurance import Person, Address, create_engine
from sqlalchemy.orm import sessionmaker,selectinload

from JsonEncode import to_json_str
from mysql.MyLog import logger

if __name__ == "__main__":
    engine = create_engine("mysql://root:123456@localhost/test?charset=utf8", echo=True)
    session_obj_ref = sessionmaker(bind=engine)
    session_instance = session_obj_ref()
    person_query = session_instance.query(Person)
    person__get = person_query.get(2)
    logger.info("person返回值：%s", to_json_str(person__get))
    # logger.info("sssssssssssssssssssssss")
    # logger.info("address：%s",to_json_str(person__get.address))
    # address_query = session_instance.query(Address)
    # address_query_get = address_query.get(2)
    # logger.info("address返回：%s", to_json_str(address_query_get.persons))
    # logger.info("address返回person：%s", to_json_str(address_query_get.persons[0].addressList))
