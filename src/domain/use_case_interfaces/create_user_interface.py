from abc import ABC, abstractmethod


class CreateUserInterface(ABC):

    @abstractmethod
    def create_user(self, *, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> None:
        raise NotImplemented()

