# Getting Started
[![CircleCI](https://circleci.com/gh/ahmednafies/sanic_camelcase_middleware.svg?style=shield)](https://circleci.com/gh/ahmednafies/sanic_camelcase_middleware) [![codecov](https://codecov.io/gh/ahmednafies/sanic_camelcase_middleware/branch/master/graph/badge.svg)](https://codecov.io/gh/ahmednafies/sanic_camelcase_middleware)



Full code on [github](https://github.com/ahmednafies/sanic_camelcase_middleware).

## Install
    pip install sanic_camelcase_middelware


## Dependencies
* [pyhumps](https://pypi.org/project/pyhumps/)
* [sanic](https://pypi.org/project/sanic/)

## Example
    from sanic import Sanic
    from sanic_camelcase_middleware import Camelize

    app = Sanic(__name__)
    Camelize(app)
