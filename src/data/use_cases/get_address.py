from typing import List
from src.domain.use_case_interfaces.get_address_interface import GetAddressInterface
from src.infra.db.repositories.address_repository_interface import AddressRepositoryInterface


class GetAddress(GetAddressInterface):

    def __init__(self, use_case: AddressRepositoryInterface):
        self.user_case = use_case

    def get_address(self) -> List:
        return self.user_case.get_address()
