# Full example

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
