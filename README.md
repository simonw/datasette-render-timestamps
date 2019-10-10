# datasette-render-timestamps

[![PyPI](https://img.shields.io/pypi/v/datasette-render-timestamps.svg)](https://pypi.org/project/datasette-render-timestamps/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-render-timestamps.svg?style=svg)](https://circleci.com/gh/simonw/datasette-render-timestamps)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-render-timestamps/blob/master/LICENSE)

Datasette plugin for rendering timestamps.

Install this plugin in the same environment as Datasette to enable this new functionality:

    pip install datasette-render-timestamps

The plugin will then look out for integer numbers that are likely to be timestamps (defaults to anything that would be a number of seconds from 5 years ago to 5 years in the future - this will be configurable eventually).

These will then be rendered in a more readable format.
