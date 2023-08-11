from abc import ABC, abstractmethod


class SaveAddressInterface(ABC):

    @abstractmethod
    def save_address(
            self, *, cep: str, logradouro: str, complemento: str, bairro: str, cidade: str, uf: str
    ) -> None:
        raise NotImplemented()
