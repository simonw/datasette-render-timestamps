# datasette-render-timestamps

[![PyPI](https://img.shields.io/pypi/v/datasette-render-timestamps.svg)](https://pypi.org/project/datasette-render-timestamps/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-render-timestamps.svg?style=svg)](https://circleci.com/gh/simonw/datasette-render-timestamps)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-render-timestamps/blob/master/LICENSE)

Datasette plugin for rendering timestamps.

## Installation

Install this plugin in the same environment as Datasette to enable this new functionality:

    pip install datasette-render-timestamps

The plugin will then look out for integer numbers that are likely to be timestamps (defaults to anything that would be a number of seconds from 5 years ago to 5 years in the future - this will be configurable eventually).

These will then be rendered in a more readable format.

## Configuration

The default format is `%B %d, %Y - %H:%M:%S UTC` which renders for example: `October 10, 2019 - 07:18:29 UTC`. If you want another format, the date format can be customized using a [plugin configuration](https://datasette.readthedocs.io/en/stable/plugins.html#plugin-configuration) in a `metadata.json` file. Any format string supported by [strftime](http://strftime.org/) may be used. For example:


```json
{
    "title": "Regular metadata keys can go here too",
    "plugins": {
        "datasette-render-timestamps": {
            "format": "%Y-%m-%d-%H:%M:%S"
        }
    }
}
```

Run datasette with the `-m` flag to load the metadata config:

    datasette serve mydata.db -m metadata.json
