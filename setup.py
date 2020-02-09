from setuptools import setup

setup(
    name="sanic_camelcase_middleware",
    version="0.1",
    description="middleware for camelizing request and response for sanic",
    url="http://github.com/ahmednafies/sanic_camelcase_middleware",
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=["sanic_camelcase_middleware"],
    install_requires=["pyhumps"],
    zip_safe=False,
)
