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


class MesasController(BaseController):

    """A Controller to access Endpoints in the capstone API."""

    def __init__(self, config, call_back=None):
        super(MesasController, self).__init__(config, call_back)

    def criar_mesa(self,
                   body,
                   content_type):
        """Does a POST request to /table.

        Cria uma nova mesa a partir da informação enviada no json.

        Args:
            body (CriarMesaRequest): TODO: type description here.
            content_type (string): TODO: type description here.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/table'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)
        if (_response.text is not None) or (not str(_response.text)):
            decoded = APIHelper.json_deserialize(_response.text)

        return decoded

    def exibir_mesa(self):
        """Does a GET request to /table.

        Retorna um array com as mesas cadastradas. É possível utilizar query
        params para busca por id da mesa. (ex: /table?id=1).

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/table'
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

    def alterar_mesa(self,
                     body,
                     content_type):
        """Does a PATCH request to /table/1.

        Realiza alterações nos registros da mesa a partir do json recebido. É
        necessário informar o id por url params (ex: /table/1).

        Args:
            body (AlterarMesaRequest): TODO: type description here.
            content_type (string): TODO: type description here.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/table/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)
        if (_response.text is not None) or (not str(_response.text)):
            decoded = APIHelper.json_deserialize(_response.text)

        return decoded

    def remover_mesa(self):
        """Does a DELETE request to /table/.

        Realiza a deleção do registro de uma mesa a partir do id passado por
        url params (ex: /table/1).

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/table/'
        _query_builder = self.config.get_base_uri()
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
