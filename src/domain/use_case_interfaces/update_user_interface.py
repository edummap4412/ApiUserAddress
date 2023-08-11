from abc import ABC, abstractmethod


class UpdateUserInterface(ABC):

    @abstractmethod
    def update_user(self, *, user_id: str, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> None:
        raise NotImplemented()
