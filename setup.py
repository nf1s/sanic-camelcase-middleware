from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

VERSION = "1.1.2"

setup(
    name="sanic_camelcase_middleware",
    version=VERSION,
    description="Middleware for camelizing request and response bodies for Sanic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ahmednafies.github.io/sanic_camelcase_middleware/",
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=["sanic_camelcase_middleware"],
    install_requires=["sanic", "pyhumps"],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
)
