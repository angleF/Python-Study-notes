import MySQLdb
import pprint

"""
    使用查询cursor对象查询时建议使用sql语句中的limit进行限制行数，
    而不是使用fetchmany/fetchone函数，该类函数式将sql查询后的所有结果加载在内存中进行切割，
    这种方式将一些不需要的数据都读取了

"""

class MySqlUtil:

    def __init__(self, host, port, user, password, db, charset):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._db = db
        self._charset = charset

    def get_connect(self):
        """
            获取连接
        :return:  mysql连接对象
        """
        try:
            self._conn = MySQLdb.Connect(
                host=self._host, port=self._port, db=self._db,
                user=self._user, passwd=self._password,
                charset=self._charset
            )
            return self._conn
        except MySQLdb.Error as e:
            print("connect Mysql Error:%s" % e)

    def close_connect(self):
        """
            关闭连接
        :return: None
        """
        if self._conn:
            self._conn.close()

    def get_many(self, sql, *sql_args) -> list:
        connect_obj = self.get_connect()
        if connect_obj:
            cursor = connect_obj.cursor()
            cursor.execute(sql, *sql_args)
            # 查询结果
            cursor_fetchmany = cursor.fetchall()
            # 获取列名
            column_name = [desc[0] for desc in cursor.description]
            result_data = [dict(zip(column_name, obj)) for obj in cursor_fetchmany]
            return result_data


if __name__ == "__main__":
    mysql_util = MySqlUtil("127.0.0.1", 3306, "root", "123456", "test", "utf8")
    try:
        result_values = mysql_util.get_many(
            "SELECT * FROM `t_user` WHERE U_SEX = %s", (1,))
        pprint.pprint(result_values)
    except MySQLdb.Error as e:
        print("异常：%s" % e)
    finally:
        if mysql_util:
            mysql_util.close_connect()
