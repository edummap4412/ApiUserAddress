from src.infra.db.repositories.address_repository_interface import AddressRepositoryInterface
from src.infra.db.settings.connection import MongoDBConnectionHandle
from src.infra.db.settings.db_mongo import DefaultMongoDataBase


class AddressRepository(AddressRepositoryInterface):
    def __init__(self):
        self.user_db = MongoDBConnectionHandle(use_db=DefaultMongoDataBase())

    def get_address(self):
        with self.user_db as session:
            try:
                all_data = self.user_db.connect_database()['address'].find()
                datas = []
                for data in all_data:
                    data["_id"] = str(data["_id"])
                    datas.append(data)
                return datas

            except Exception as exception:
                session.abort_transaction()
                raise exception

    def save_address(
            self, *, cep: str, logradouro: str, complemento: str, bairro: str, cidade: str, uf: str
    ) -> None:
        with self.user_db as session:
            try:
                user_data = {
                    "cep": cep,
                    "logradouro": logradouro,
                    "complemento": complemento,
                    "bairro": bairro,
                    "cidade": cidade,
                    "uf": uf
                }
                self.user_db.connect_database()['address'].insert_one(user_data)

            except Exception as exception:
                session.abort_transaction()
                raise exception




