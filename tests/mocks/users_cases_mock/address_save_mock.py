from src.domain.use_case_interfaces.save_address_interface import SaveAddressInterface
from typing import Dict


class SaveAddressMock(SaveAddressInterface):

    def save_address(
            self, *, cep: str, logradouro: str, complemento: str, bairro: str, cidade: str, uf: str
    ) -> Dict:
        user_data = {
            "cep": cep,
            'logradouro': logradouro,
            'complemento': complemento,
            'bairro': bairro,
            'cidade': cidade,
            'uf': uf
        }

        return user_data
