from src.domain.use_case_interfaces.delete_user_interface import DeleteUserInterface
from typing import Dict


class DeleteUserMock(DeleteUserInterface):

    def delete_user(self, *, user_id: str) -> Dict:
        user_data = {
            "user_id": user_id
        }

        return user_data
