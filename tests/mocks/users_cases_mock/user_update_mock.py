from src.domain.use_case_interfaces.update_user_interface import UpdateUserInterface
from typing import Dict


class UpdateUserMock(UpdateUserInterface):

    def update_user(self, *, user_id: str, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> Dict:
        user_data = {
            "nome": nome,
            "data_de_nascimento": data_de_nascimento,
            "email": email,
            "telefone": telefone,
            "documento": documento
        }

        return user_data
