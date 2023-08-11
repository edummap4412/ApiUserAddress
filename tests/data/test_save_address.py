from tests.mocks.address_repository_mock.address_repository_mock import AddressRepositoryMock
from src.data.use_cases.save_address import SaveAddress


def test_use_cases_create_user():
    user_repository = AddressRepositoryMock()
    use_case = SaveAddress(user_repository)
    use_case.save_address(
        cep='123456',
        logradouro="logradouro",
        complemento="complemento",
        bairro="bairro",
        cidade="cidade",
        uf="uf"
    )
    user = user_repository.created_attributes
    assert user['logradouro'] == "logradouro"
    assert user['complemento'] == "complemento"

