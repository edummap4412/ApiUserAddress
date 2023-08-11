from abc import ABC, abstractmethod


class GetUserInterface(ABC):

    @abstractmethod
    def get_user(self) -> None:
        raise NotImplemented()

