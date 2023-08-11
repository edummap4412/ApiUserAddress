from abc import ABC, abstractmethod


class AddressRepositoryInterface(ABC):

    @abstractmethod
    def get_address(self):
        raise NotImplemented()

    @abstractmethod
    def save_address(
            self, *,cep: str, logradouro: str, complemento: str, bairro: str, cidade: str, uf: str
    ) -> None:
        raise NotImplemented()

