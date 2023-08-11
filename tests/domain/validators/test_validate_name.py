import pytest
from src.domain.validators.validation_name import ValidateName


def test_validate_name_valid():
    nome = "Eduardo Michael"
    valid_name = ValidateName(nome=nome)

    assert valid_name.get_value() == nome


def test_validate_name_invalid():
    with pytest.raises(ValueError, match="Nome invalido."):
        nome = "Eduardo Michael123_@"
        ValidateName(nome=nome)
