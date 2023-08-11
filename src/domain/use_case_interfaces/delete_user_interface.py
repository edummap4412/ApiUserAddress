from abc import ABC, abstractmethod


class DeleteUserInterface(ABC):

    @abstractmethod
    def delete_user(self, *, user_id: str) -> None:
        raise NotImplemented()

