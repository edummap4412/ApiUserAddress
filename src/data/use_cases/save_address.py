from src.domain.use_case_interfaces.save_address_interface import SaveAddressInterface
from src.infra.db.repositories.address_repository import AddressRepositoryInterface
from typing import Dict


class SaveAddress(SaveAddressInterface):
    def __init__(self, use_case: AddressRepositoryInterface):
        self.use_case = use_case

    def save_address(self, *, cep: str, logradouro: str, complemento: str, bairro: str, cidade: str, uf: str) -> Dict:
        self.use_case.save_address(
                cep=cep,
                logradouro=logradouro,
                complemento=complemento,
                bairro=bairro,
                cidade=cidade,
                uf=uf
        )

        return self.__format_response(
            cep=cep,
            logradouro=logradouro,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            uf=uf
        )

    @classmethod
    def __format_response(cls, *, cep: str, logradouro: str, complemento: str, bairro: str, cidade: str, uf: str) -> Dict:
        return {"sucesso": "true",
                "endereco":
                    {
                        "cep": cep,
                        "logr": logradouro,
                        "compl": complemento,
                        "bairro": bairro,
                        "cidade": cidade,
                        "uf": uf
                    }
                }

