from pymongo import MongoClient
from src.infra.db.settings.db_mongo import DefaultMongoDataBase


class MongoDBConnectionHandle:
    def __init__(self, *, use_db: DefaultMongoDataBase):
        self.__conection_string = 'mongodb://admin:adminpassword@localhost:27017/admin'
        self.use_db = use_db
        self.client = None

    def __enter__(self):
        self.client = MongoClient(self.__conection_string)
        self.session = self.client.start_session()
        return self

    def connect_database(self):
        return self.client[self.use_db.db_mongo]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.end_session()
        self.client.close()
