import pymysql
pymysql.install_as_MySQLdb()
import databases
from sqlalchemy import create_engine, MetaData
metadata = MetaData()
from config import DBHOST, DBPORT, DATABASE, DBUSER, DBPASSWORD

class Connection:
    def __init__(self, dbhost, dbport, database, dbuser, dbpassword, create_tables = True):
        self.__dbhost = dbhost
        self.__dbport = dbport
        self.__database = database
        self.__dbuser = dbuser
        self.__dbpassword =  dbpassword
        self.__connection_string = self.__get_connection_string()
        self.__db = databases.Database(self.__connection_string)
        self.__engine = self.__db_connect()
        if create_tables:
            self.create_tables()

    def __get_connection_string(self):
        dbhost = self.__dbhost
        dbuser = self.__dbuser
        dbpassword = self.__dbpassword
        dbport = self.__dbport
        dbbase = self.__database
        return  f'mysql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbbase}'

    def __db_connect(self):
        return create_engine(self.__connection_string)

    def get_engine(self):
        return  self.__engine

    def get_connection(self):
        try:
            return self.__engine.connect()
        except:
            return None

    def get_db(self):
        return self.__db

    def create_tables(self):
        metadata.create_all(self.get_engine())

    def execute_sql(self, sql):
        rs = None
        with self.__engine.connect() as con:
            rs = con.execute(sql)
        return rs

connection = Connection(dbhost=DBHOST, dbport=DBPORT, database=DATABASE, dbuser=DBUSER, dbpassword=DBPASSWORD)