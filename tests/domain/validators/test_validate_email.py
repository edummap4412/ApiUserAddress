import pytest
from src.domain.validators.validate_email import ValidateEmail


def test_validated_email_valid():
    email = 'email@valido.com'
    validated_email = ValidateEmail(email=email)

    assert validated_email.get_value() == email


def test_validated_email_invalid():
    with pytest.raises(ValueError, match='Email invalido'):
        email = 'email_valido.com'
        ValidateEmail(email=email)
