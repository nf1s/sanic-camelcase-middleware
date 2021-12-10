# -*- coding: utf-8 -*-
""" Sanic camelcase middleware module

Middleware is checks if a request has a body,
if a request has a body, middleware will decode the body
and decamilize (camelCase => snake_case) its keys
then encode it back again.

example if the request.body = {"myVal":"Hello_world"},
the middleware will convert it to {"my_val":"Hello_world"}

"""
from json import dumps, loads

from humps import camelize, decamelize

__author__ = "Ahmed Nafies Okasha Mohamed <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"
__license__ = "MIT"
__version__ = "1.3.1"


class Camelize:
    def __init__(
        self,
        app,
        decamelize_request: bool = True,
        camelize_response: bool = True,
    ):
        @app.middleware("request")
        def request_to_snake_case(request):
            """Function converts request body to snake_case
            Args:
                request: Sanic HttpRequest Object
            """
            if decamelize_request and request.body:
                request.body = bytes(
                    dumps(decamelize(loads(request.body))), "utf-8"
                )

        @app.middleware("response")
        def response_to_camel(request, response):
            """Function converts response body to camelcase
            Args:
                request (HttpRequest): Sanic HttpRequest Object
                response (HttpRequest): Sanic HttpResponse Object
            """
            if camelize_response and response.body:
                response.body = bytes(
                    dumps(camelize(loads(response.body))), "utf-8"
                )
