from src.domain.use_case_interfaces.delete_user_interface import DeleteUserInterface
from src.infra.db.repositories.user_repository_interface import UserRepositoryInterface
from src.errors.types.http_not_found import HttpNotFoundError


class DeleteUser(DeleteUserInterface):

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def delete_user(self, *, user_id: str):
        try:
            return self.user_repository.delete_user(user_id=user_id)
        except Exception as e:
            raise HttpNotFoundError(message="Usuario não encontrado")
