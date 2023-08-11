from abc import ABC, abstractmethod


class ValidatorInterface(ABC):
    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_value(self) -> str:
        raise NotImplementedError
