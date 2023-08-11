from src.domain.use_case_interfaces.get_user_interface import GetUserInterface
from src.infra.db.repositories.user_repository_interface import UserRepositoryInterface
from typing import List


class GetUser(GetUserInterface):

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def get_user(self) -> List:
        return self.user_repository.get_user()

