# Sanic Camelcase Middleware

[![CircleCI](https://circleci.com/gh/ahmednafies/sanic_camelcase_middleware.svg?style=shield)](https://circleci.com/gh/ahmednafies/sanic_camelcase_middleware) [![codecov](https://codecov.io/gh/ahmednafies/sanic_camelcase_middleware/branch/master/graph/badge.svg)](https://codecov.io/gh/ahmednafies/sanic_camelcase_middleware) [![Downloads](https://pepy.tech/badge/sanic-camelcase-middleware)](https://pepy.tech/project/sanic-camelcase-middleware) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ahmednafies/sanic_camelcase_middleware) ![GitHub](https://img.shields.io/github/license/ahmednafies/sanic_camelcase_middleware)

Middleware for camelizing request and response bodies for sanic

Full documentation can be found [here](https://ahmednafies.github.io/sanic_camelcase_middleware/)

## How to install

```bash
    pip install sanic-camelcase-middlware
```

### Example

```python
    from sanic import Sanic
    from sanic_camelcase_middleware import Camelize

    app = Sanic(__name__)
    Camelize(app)
```

### Full example

```python
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
```

### To disable the middleware for request payload

```python
    from sanic import Sanic
    from sanic_camelcase_middleware import Camelize

    app = Sanic(__name__)

    # default `decamelize_request=True`
    Camelize(app, decamelize_request=False)
```

### To disable the middleware for response body

```python
    from sanic import Sanic
    from sanic_camelcase_middleware import Camelize

    app = Sanic(__name__)

    # default `camelize_response=True`
    Camelize(app, camelize_response=False)
```
