from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="sanic_camelcase_middleware",
    version="0.0.1",
    description="Middleware for camelizing request and response bodies for sanic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/ahmednafies/sanic_camelcase_middleware",
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=["sanic_camelcase_middleware"],
    install_requires=["pyhumps"],
    zip_safe=False,
)
