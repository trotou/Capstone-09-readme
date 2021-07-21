# -*- coding: utf-8 -*-

"""
capstone

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from capstone.api_helper import APIHelper
from capstone.configuration import Server
from capstone.controllers.base_controller import BaseController
from capstone.http.auth.o_auth_2 import OAuth2


class GerentesController(BaseController):

    """A Controller to access Endpoints in the capstone API."""

    def __init__(self, config, call_back=None):
        super(GerentesController, self).__init__(config, call_back)

    def exibir_gerentes(self):
        """Does a GET request to /manager.

        Endpoint destinado à criação de gerente diretamente na tabela managers
        (gerentes). É utilizado de forma automatizada quando realizada a
        criação de usuário do tipo 1 (tabela users).

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/manager'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)
        if (_response.text is not None) or (not str(_response.text)):
            decoded = APIHelper.json_deserialize(_response.text)

        return decoded

    def alterar_gerente(self,
                        body):
        """Does a PATCH request to /manager/2.

        Realiza alteração de nome ou cpf do gerente selecionado por id,
        através de url params.

        Args:
            body (CriarGerenteRequest): TODO: type description here.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/manager/2'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)
        if (_response.text is not None) or (not str(_response.text)):
            decoded = APIHelper.json_deserialize(_response.text)

        return decoded

    def remover_gerente(self):
        """Does a DELETE request to /manager/4.

        Remove o gerente selecionado por id, através de url params.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/manager/4'
        _query_builder = self.config.get_base_uri(Server.SERVER_1)
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)
        if (_response.text is not None) or (not str(_response.text)):
            decoded = APIHelper.json_deserialize(_response.text)

        return decoded
