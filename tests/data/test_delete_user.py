from tests.mocks.user_repository_mock.user_repository_mock import UserRepositoryMock
from src.data.use_cases.delete_user import DeleteUser


def test_use_case_delete_user():
    user_repository = UserRepositoryMock()
    use_case = DeleteUser(user_repository)

    get_id = user_repository.get_user_attributes[0]['user1']['user_id']
    assert user_repository.get_user_attributes is not None
    use_case.delete_user(user_id=get_id)
    assert user_repository.get_user_attributes == []


