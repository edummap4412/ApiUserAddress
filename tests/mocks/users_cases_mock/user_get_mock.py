from src.domain.use_case_interfaces.get_user_interface import GetUserInterface
from typing import List


class GetUserMock(GetUserInterface):
    def __init__(self):
        self.get_user_attributes = [{'user1': {
            "nome": "Michael",
            "data_de_nascimento": "30/06/1994",
            "email": "eduardo@email.com",
            "telefone": '+123(45) 0987-1234',
            "documento": "789.123.456-08"
        }}]

    def get_user(self) -> List:
        return self.get_user_attributes
