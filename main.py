# -*- coding: utf-8 -*-
"""Sample main.py used for running tests for middleware

"""
from sanic import Sanic
from sanic import response
from sanic.response import json
from sanic_camelcase_middleware import Camelize

app = Sanic(__name__)

Camelize(app)


@app.route("/", methods=["GET"])
async def index(request):
    return json({"is_camelcase": True, "message": "Hello_world"})


@app.route("/post", methods=["POST"])
async def post(request):
    return json({"is_camelcase": True, "message": request.json})


@app.route("/empty", methods=["PUT"])
async def empty_response(request):
    return response.empty()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
