import pytest
from src.domain.validators.validate_phone_number import ValidatePhoneNumber


def test_validate_phone_number_valid():
    telefone = "+123(45) 0987-1234"
    validate = ValidatePhoneNumber(telefone=telefone)

    assert validate.get_value() == telefone


def test_validate_phone_number_invalid():
    with pytest.raises(ValueError, match='Numero de telefone invalido'):
        telefone = "+123 45 0987-1234"
        ValidatePhoneNumber(telefone=telefone)
