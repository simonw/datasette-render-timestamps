from setuptools import setup
import os

VERSION = "1.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-render-timestamps",
    description="Datasette plugin for rendering timestamps",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-render-timestamps",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_render_timestamps"],
    entry_points={"datasette": ["render_timestamps = datasette_render_timestamps"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest"]},
    tests_require=["datasette-render-timestamps[test]"],
)
