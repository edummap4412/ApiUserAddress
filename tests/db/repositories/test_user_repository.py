import pytest
from src.infra.db.repositories.user_repository import UserRepository


@pytest.mark.skip("Sensitive Tests")
def test_user_repository_create_user():
    user_repository = UserRepository()
    user_repository.create_user(
        nome="Eduardo",
        data_de_nascimento='30/06/1994',
        email='eduaro@gmail.com',
        telefone='(11) 940885674',
        documento='123.324.454-55'
    )


@pytest.mark.skip("Sensitive Tests")
def test_user_repository_get_user():
    user_repository = UserRepository()
    print(user_repository.get_user())


@pytest.mark.skip("Sensitive Tests")
def test_user_repository_update_email_user():
    user_repository = UserRepository()
    user_repository.update_user(
        user_id='123456789',
        nome="Eduardo",
        data_de_nascimento='30/06/1994',
        email='eduardomascarenhas@gmail.com',
        telefone='(11) 940885674',
        documento='123456789'
    )


@pytest.mark.skip("Sensitive Tests")
def test_user_repository_delete_user():
    user_repository = UserRepository()
    user_repository.delete_user(user_id='123456789')
