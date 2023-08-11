from typing import Dict

from src.infra.db.repositories.address_repository_interface import AddressRepositoryInterface


class AddressRepositoryMock(AddressRepositoryInterface):

    def __init__(self):
        self.created_attributes = {}
        self.get_attributes = [{
            'address1': {
                'cep' : '123456',
                'logradouro': 'logradouro',
                'complemento': 'complemento',
                'bairro': 'bairro',
                'cidade': 'cidade',
                'uf': 'uf'
            }
        }]

    def save_address(
            self, *, cep: str, logradouro: str, complemento: str, bairro: str, cidade: str, uf: str
    ) -> Dict:

        address_data = {
            'logradouro': logradouro,
            'complemento': complemento,
            'bairro': bairro,
            'cidade': cidade,
            'uf': uf
        }
        self.created_attributes = address_data
        return self.created_attributes

    def get_address(self):
        return self.get_attributes

