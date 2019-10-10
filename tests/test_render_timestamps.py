from datasette_render_timestamps import render_cell


def test_render_timestamps():
    assert "October 10, 2019 - 00:18:29" == render_cell(1570691909)


def test_do_not_render_low_numbers():
    assert None == render_cell(1)


def test_do_not_render_high_numbers():
    assert None == render_cell(15706919090)
