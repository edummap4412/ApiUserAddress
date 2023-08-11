from src.domain.use_case_interfaces.create_user_interface import CreateUserInterface
from typing import Dict


class CreateUserMock(CreateUserInterface):

    def create_user(self, *, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> Dict:
        user_data = {
            "nome": nome,
            "data_de_nascimento": data_de_nascimento,
            "email": email,
            "telefone": telefone,
            "documento": documento
        }

        return user_data

