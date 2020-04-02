import io
import re

from setuptools import setup

with io.open("README.md") as f:
    long_description = f.read()

with io.open("sanic_camelcase_middleware/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="sanic_camelcase_middleware",
    version=version,
    description="Middleware for camelizing request and response bodies for Sanic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ahmednafies.github.io/sanic_camelcase_middleware/",
    project_urls={
        "Documentation": "https://ahmednafies.github.io/sanic_camelcase_middleware/",
        "Source": "https://github.com/ahmednafies/sanic_camelcase_middleware",
    },
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=["sanic_camelcase_middleware"],
    install_requires=["sanic", "pyhumps"],
    python_requires=">=3.6",
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
