import pytest
from src.main.sdks.via_cep.get_cep import ViaCepSdk


def test_sdk_viacep_get_cep_valid():
    via_cep = ViaCepSdk()

    get_cep = via_cep.get_address_by_cep('03813-000')

    assert get_cep['cep'] == '03813-000'
    assert get_cep['logradouro'] == 'Rua Figueira da Polinésia'
    assert get_cep['localidade'] == 'São Paulo'


def test_sdk_viacep_get_cep_invalid():
    with pytest.raises(Exception, match='CEP invalido , digite corretamente'):
        via_cep = ViaCepSdk()
        via_cep.get_address_by_cep('03813-0')
