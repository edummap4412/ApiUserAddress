import pytest
from src.domain.validators.validate_brazilian_document import ValidateBrazilianDocument


def test_validate_brazilian_document_valid():
    documento = '964.157.430-23'
    valide_braziliaan_document = ValidateBrazilianDocument(documento=documento)

    assert valide_braziliaan_document.get_value() == documento


def test_validate_brazilian_document_invalid():
    with pytest.raises(ValueError, match='Documento Invalido'):
        documento = '123.157.430-23'
        ValidateBrazilianDocument(documento=documento)
