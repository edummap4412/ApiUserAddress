from abc import ABC, abstractmethod


class GetAddressInterface(ABC):

    @abstractmethod
    def get_address(self):
        pass
