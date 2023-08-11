from src.infra.db.repositories.user_repository import UserRepository
from src.data.use_cases.delete_user import DeleteUser
from src.presentation.controllers.controller_delete_user import ControllerDeleteUser


def delete_user_composer():
    repository = UserRepository()
    use_case = DeleteUser(repository)
    controller = ControllerDeleteUser(use_case)
    return controller.handle
