import requests
import xml.etree.ElementTree as ET
import logging

from src.main.sdks.via_cep.viacep_interface import ViaCepSdkInterface
from src.errors.types.http_bad_request import HttpBadResquestError


class ViaCepSdk(ViaCepSdkInterface):
    def __init__(self):
        self.base_url = "https://viacep.com.br/ws/{}/xml"

    def get_address_by_cep(self, cep):
        try:
            url = self.base_url.format(cep)
            response = requests.get(url)

            response.raise_for_status()

            root = ET.fromstring(response.content)
            address_data = {}
            for child in root:
                address_data[child.tag] = child.text

            return address_data

        except requests.exceptions.RequestException as e:
            logging.error(str(e))
            raise HttpBadResquestError('CEP invalido , digite corretamente')

