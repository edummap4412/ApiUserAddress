from src.infra.db.repositories.user_repository_interface import UserRepositoryInterface
from typing import List, Dict


class UserRepositoryMock(UserRepositoryInterface):
    def __init__(self):
        self.get_user_attributes = [{'user1': {
            "user_id": "12345",
            "nome": "Michael",
            "data_de_nascimento": "30/06/1994",
            "email": "eduardo@email.com",
            "telefone": '+123(45) 0987-1234',
            "documento": "789.123.456-08"
        }}]

    def create_user(self, *, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> Dict:
            user_data = {
                "nome": nome,
                "data_de_nascimento": data_de_nascimento,
                "email": email,
                "telefone": telefone,
                "documento": documento
            }

            return user_data

    def get_user(self) -> List:
        return self.get_user_attributes

    def update_user(
            self, *,
            user_id: str = None,
            nome: str = None,
            data_de_nascimento: str = None,
            email: str = None,
            telefone: str = None,
            documento: str = None
    ):
        get_data = self.get_user_attributes[0]['user1']
        get_data['nome'] = nome if nome else get_data.get('nome')
        get_data['data_de_nascimento'] = data_de_nascimento if data_de_nascimento else get_data.get('data_de_nascimento')
        get_data['email'] = email if email else get_data.get('email')
        get_data['telefone'] = telefone if telefone else get_data.get('telefone')
        get_data['documento'] = documento if documento else get_data.get('documento')

        return self

    def delete_user(self, *, user_id: str) -> List:
        for user_dict in self.get_user_attributes:
            if user_dict['user1']['user_id'] == user_id:
                self.get_user_attributes.remove(user_dict)

        return self.get_user_attributes
