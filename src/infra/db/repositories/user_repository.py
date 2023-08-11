from src.infra.db.repositories.user_repository_interface import UserRepositoryInterface
from src.infra.db.settings.connection import MongoDBConnectionHandle
from src.infra.db.settings.db_mongo import DefaultMongoDataBase
from bson import ObjectId


class UserRepository(UserRepositoryInterface):
    def __init__(self):
        self.user_db = MongoDBConnectionHandle(use_db=DefaultMongoDataBase())

    def create_user(self, *, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> None:
        with self.user_db as session:
            try:
                user_data = {
                    "nome": nome,
                    "data_de_nascimento": data_de_nascimento,
                    "email": email,
                    "telefone": telefone,
                    "documento": documento
                }
                self.user_db.connect_database()['user'].insert_one(user_data)

            except Exception as exception:
                session.abort_transaction()
                raise exception

    def get_user(self):
        with self.user_db as session:
            try:
                all_data = self.user_db.connect_database()['user'].find()
                datas = []
                for data in all_data:
                    data["_id"] = str(data["_id"])
                    datas.append(data)
                return datas

            except Exception as exception:
                session.abort_transaction()
                raise exception

    def update_user(self, *, user_id: str, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> None:
        with self.user_db as session:
            try:
                filter_query = {"_id": ObjectId(user_id)}
                update_query = {
                    "$set": {
                        "nome": nome,
                        "data_de_nascimento": data_de_nascimento,
                        "email": email,
                        "telefone": telefone
                    }
                }
                self.user_db.connect_database()['user'].update_one(filter_query, update_query)
            except Exception as exception:
                session.abort_transaction()
                raise exception

    def delete_user(self, *, user_id: str) -> None:
        with self.user_db as session:
            try:
                filter_query = {"_id": ObjectId(user_id)}
                self.user_db.connect_database()['user'].delete_one(filter_query)
            except Exception as exception:
                session.abort_transaction()
                raise exception


