from abc import ABC, abstractmethod
from typing import List


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create_user(self, *, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> None:
        raise NotImplemented()

    @abstractmethod
    def get_user(self) -> List:
        raise NotImplemented()

    @abstractmethod
    def update_user(self, *, user_id: str, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> None:
        raise NotImplemented()

    @abstractmethod
    def delete_user(self, *, user_id: str) -> None:
        raise NotImplemented()
