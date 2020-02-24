# -*- coding: utf-8 -*-
""" Sanic camelcase middleware tests module
"""
import json
from humps import camelize
from main import app


def test_get_request():
    """test_get_request function tests get requests for middleware
    The purpose of this test is to check if the middleware would work if the request
    has no payload in case of "GET" requests.
    However the respons should be camilized.
    """
    request, response = app.test_client.get("/")
    assert response.status == 200
    assert response.json == {"isCamelcase": True, "message": "Hello_world"}


def test_request_post_body_snakecased():
    """test_request_post_body_snakecased function tests post request with snake_cased keys.
    The expected return should be camelCased response body
    """
    data = {"my_value": "test_value"}
    request, response = app.test_client.post("/post", data=json.dumps(data))
    assert response.status == 200
    assert response.json == {"isCamelcase": True, "message": camelize(data)}


def test_request_post_body_camelcased():
    """test_request_post_body_camelcased function tests post request with camelCased keys.
    The expected return should be camelCased response body as well
    """
    data = {"myValue": "test_value"}
    request, response = app.test_client.post("/post", data=json.dumps(data))
    assert response.status == 200
    assert response.json == {"isCamelcase": True, "message": camelize(data)}


def test_request_post_body_without_response_body():
    """test_request_post_body_without_response_body function
    checks the case where reponse does not contain a body
    """
    data = {"my_value": "test_value"}
    request, response = app.test_client.put("/empty", data=json.dumps(data))
    assert response.status == 204
