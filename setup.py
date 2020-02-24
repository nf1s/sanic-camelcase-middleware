from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

VERSION = 1.0.0

class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setup(
    name="sanic_camelcase_middleware",
    version=VERSION,
    description="Middleware for camelizing request and response bodies for Sanic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/ahmednafies/sanic_camelcase_middleware",
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=["sanic_camelcase_middleware"],
    install_requires=["sanic", "pyhumps"],
    zip_safe=False,
)
