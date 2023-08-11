from src.data.use_cases.create_user import CreateUser
from tests.mocks.user_repository_mock.user_repository_mock import UserRepositoryMock


def test_use_cases_create_user():

    user_repository = UserRepositoryMock()
    use_case = CreateUser(user_repository)

    user = use_case.create_user(
        nome="Michael",
        data_de_nascimento="30/06/1994",
        email="eduardo@email.com",
        telefone='+123(45) 0987-1234',
        documento='964.157.430-23'
    )
    assert user['data']['nome'] == "Michael"
    assert user['data']['email'] == "eduardo@email.com"
    assert user['data']['telefone'] == "+123(45) 0987-1234"

