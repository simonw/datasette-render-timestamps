from unittest import mock
from datasette.app import Datasette
from datasette_render_timestamps import render_cell


def mock_plugin_config(*args, **kwargs):
    return {"format": "%Y-%m-%d-%H:%M:%S"}


def test_render_timestamps():
    assert "October 10, 2019 - 07:18:29 UTC" == render_cell(
        1570691909, None, None, None, Datasette([])
    )


def test_do_not_render_low_numbers():
    assert None == render_cell(
        1, None, None, None, Datasette([])
    )


def test_do_not_render_high_numbers():
    assert None == render_cell(
        15706919090, None, None, None, Datasette([])
    )


@mock.patch(
    "datasette.app.Datasette.plugin_config",
    mock_plugin_config,
)
def test_custom_format():
    assert "2019-10-10-07:18:29" == render_cell(
        1570691909, None, None, None, Datasette([])
    )
