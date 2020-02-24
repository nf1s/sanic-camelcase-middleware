# -*- coding: utf-8 -*-
""" Sanic camelcase middleware module

Middleware is checks if a request has a body,
if a request has a body,  middleware will decode the body and decamilize (camelCase => snake_case) its keys
then encode it back again.

example if the request.body = {"myVal":"Hello_world"},
the middleware will convert it to {"my_val":"Hello_world"}

"""
from json import loads, dumps
from humps import camelize, decamelize


class Camelize:
    def __init__(self, app):
        @app.middleware("request")
        async def request_to_snake_case(request):
            """Function converts request body to snake_case
            
            Args:
                request: Sanic HttpRequest Object
            """
            if request.body:
                request.body = bytes(dumps(decamelize(loads(request.body))), "utf-8")

        @app.middleware("response")
        async def response_to_camel(request, response):
            """Function converts response body to camelcase
            
            Args:
                request (HttpRequest): Sanic HttpRequest Object
                response (HttpRequest): Sanic HttpResponse Object
            """
            if response.body:
                response.body = bytes(dumps(camelize(loads(response.body))), "utf-8")

