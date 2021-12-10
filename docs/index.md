# Getting Started

[![CircleCI](https://circleci.com/gh/nf1s/sanic-camelcase-middleware.svg?style=shield)](https://circleci.com/gh/nf1s/sanic-camelcase-middleware) [![codecov](https://codecov.io/gh/nf1s/sanic-camelcase-middleware/branch/master/graph/badge.svg)](https://codecov.io/gh/nf1s/sanic-camelcase-middleware) [![Downloads](https://pepy.tech/badge/sanic-camelcase-middleware)](https://pepy.tech/project/sanic-camelcase-middleware) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/nf1s/sanic-camelcase-middleware) ![GitHub](https://img.shields.io/github/license/nf1s/sanic-camelcase-middleware)

Full code on [github](https://github.com/nf1s/sanic-camelcase-middleware).

## Install

```bash
    pip install sanic_camelcase_middelware
```

## Dependencies

- [pyhumps](https://pypi.org/project/pyhumps/)
- [sanic](https://pypi.org/project/sanic/)

## Example

```python
    from sanic import Sanic
    from sanic_camelcase_middleware import Camelize

    app = Sanic(__name__)
    Camelize(app)
```
