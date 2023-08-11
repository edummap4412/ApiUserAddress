from tests.mocks.address_repository_mock.address_repository_mock import AddressRepositoryMock
from src.data.use_cases.get_address import GetAddress


def test_use_cases_create_user():
    user_repository = AddressRepositoryMock()
    use_case = GetAddress(user_repository)
    use_case.get_address()

    user = user_repository.get_attributes[0]['address1']

    assert user['logradouro'] == "logradouro"
    assert user['complemento'] == "complemento"

