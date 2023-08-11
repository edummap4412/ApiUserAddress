from abc import ABC, abstractmethod


class ViaCepSdkInterface(ABC):

    @abstractmethod
    def get_address_by_cep(self, cep):
        raise NotImplemented()
