[![CircleCI](https://circleci.com/gh/ahmednafies/sanic_camelcase_middleware.svg?style=shield)](https://circleci.com/gh/ahmednafies/sanic_camelcase_middleware) ![](./coverage.svg)

# sanic_camelcase_middlware
Middleware for camelizing request and response bodies for sanic

Full documentation can be found [here](https://ahmednafies.github.io/sanic_camelcase_middleware/)

## How to install
    pip install sanic-camelcase-middlware

### Example
    from sanic import Sanic
    from sanic_camelcase_middleware import Camelize

    app = Sanic(__name__)
    Camelize(app)

### Full example
    from sanic import Sanic
    from sanic.response import json
    from sanic_camelcase_middleware import Camelize

    app = Sanic(__name__)

    Camelize(app)


    @app.route("/post", methods=["POST"])
    async def test(request):
        return json("is_camelcase": True, "message": request.json})


    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8000)
