import pytest
from src.infra.db.repositories.address_repository import AddressRepository


@pytest.mark.skip("Sensitive Tests")
def test_user_repository_create_user():
    user_repository = AddressRepository()
    user_repository.save_address(
            cep='1234567',
            logradouro='logradouro',
            complemento='complemento',
            bairro='bairro',
            cidade='cidade',
            uf='uf'
        )


@pytest.mark.skip("Sensitive Tests")
def test_user_repository_get_user():
    user_repository = AddressRepository()
    print(user_repository.get_address())
