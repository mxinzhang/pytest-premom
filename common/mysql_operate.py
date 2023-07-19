import pymysql
import os
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["mysql"]

DB_CONF = {
    "host": data["MYSQL_HOST"],
    "port": int(data["MYSQL_PORT"]),
    "user": data["MYSQL_USER"],
    "password": data["MYSQL_PASSWD"],
    "db": data["MYSQL_DB"]
}


class MysqlDb():
    """
    A class representing a MySQL database connection.

    Attributes:
        conn: A pymysql connection object representing the database connection.
        cur: A pymysql cursor object for executing queries.
    """

    def __init__(self, db_conf=DB_CONF):
        """
        Initializes a new instance of the MysqlDb class.

        Args:
            db_conf: A dictionary containing the database connection configuration.
        """
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        """
        Performs cleanup operations before the object is deleted.
        Closes the cursor and the database connection.
        """
        self.cur.close()
        self.conn.close()

    def select_db(self, sql):
        """
        Executes a SELECT query on the database.

        Args:
            sql: A string representing the SQL query to execute.

        Returns:
            A list of dictionaries representing the query results.
        """
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """
        Executes an UPDATE/INSERT/DELETE query on the database.

        Args:
            sql: A string representing the SQL query to execute.
        """
        try:
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("An error occurred while operating MySQL, Reason: {}".format(e))
            self.conn.rollback()


db = MysqlDb(DB_CONF)
