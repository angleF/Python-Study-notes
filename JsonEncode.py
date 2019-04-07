import json
from sqlalchemy.ext.declarative import DeclarativeMeta
import datetime


class CustomizeEncode(json.JSONEncoder):

    def default(self, obj):
        """
         只要检查到bytes类型数据就将其转为str类型
        :param o:
        :return:
        """

        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:  # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    elif is_super_instance(data, DeclarativeMeta):
                        fields[field] = json.dumps(data, cls=CustomizeEncode, ensure_ascii=False)
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def to_json_str(obj):
    return json.dumps(obj, cls=CustomizeEncode, ensure_ascii=False)


def is_super_instance(obj, cls):
    # 使用传统的遍历循环
    #     bases__ = obj.__class__.__bases__
    #     for base_obj in bases__:
    #         if isinstance(base_obj, cls):
    #             return True
    #         break
    #     return False
    # 使用filter函数
    # return list(filter(lambda base_obj: isinstance(base_obj, cls), obj.__class__.__bases__))
    # 使用列表推导
    return [base_obj for base_obj in obj.__class__.__bases__ if isinstance(base_obj, cls)]
