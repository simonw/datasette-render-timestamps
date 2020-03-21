from unittest import mock
from datasette.app import Datasette
from datasette_render_timestamps import render_cell
import datetime
import pytest


@pytest.fixture
def timestamp_within_five_years():
    current_year = datetime.date.today().year
    dt = datetime.datetime(current_year, 10, 10, 7, 18, 29)
    return int(dt.replace(tzinfo=datetime.timezone.utc).timestamp())


def test_render_timestamps(timestamp_within_five_years):
    assert "October 10, {} - 07:18:29 UTC".format(
        datetime.date.today().year
    ) == render_cell(timestamp_within_five_years, None, None, None, Datasette([]))


def test_do_not_render_low_numbers():
    assert None == render_cell(1, None, None, None, Datasette([]))


def test_do_not_render_high_numbers(timestamp_within_five_years):
    assert None == render_cell(
        timestamp_within_five_years * 1000, None, None, None, Datasette([])
    )


def test_custom_format(timestamp_within_five_years):
    assert "{}-10-10 07:18:29".format(datetime.date.today().year) == render_cell(
        timestamp_within_five_years,
        column="timestamp",
        table="mytable",
        database="mydatabase",
        datasette=Datasette(
            [],
            metadata={
                "plugins": {
                    "datasette-render-timestamps": {"format": "%Y-%m-%d %H:%M:%S"}
                }
            },
        ),
    )


@pytest.mark.parametrize(
    "metadata",
    [
        # Table level
        {
            "databases": {
                "mydatabase": {
                    "tables": {
                        "mytable": {
                            "plugins": {
                                "datasette-render-timestamps": {
                                    "format": "%Y-%m-%d %H:%M:%S",
                                    "columns": ["timestamp"],
                                }
                            }
                        }
                    }
                }
            }
        },
        # Database level
        {
            "databases": {
                "mydatabase": {
                    "plugins": {
                        "datasette-render-timestamps": {
                            "format": "%Y-%m-%d %H:%M:%S",
                            "columns": ["timestamp"],
                        }
                    }
                }
            }
        },
        # Global level
        {
            "plugins": {
                "datasette-render-timestamps": {
                    "format": "%Y-%m-%d %H:%M:%S",
                    "columns": ["timestamp"],
                }
            }
        },
    ],
)
def test_explicit_column(metadata):
    # Without metadata should be None
    assert None == render_cell(
        1286720309,
        column="timestamp",
        table="mytable",
        database="mydatabase",
        datasette=Datasette([]),
    )
    # With metadata should render correctly
    assert "2010-10-10 14:18:29" == render_cell(
        1286720309,
        column="timestamp",
        table="mytable",
        database="mydatabase",
        datasette=Datasette([], metadata=metadata),
    )


def test_disable_auto_detection_with_explicit_column_empty_list(
    timestamp_within_five_years,
):
    # Without metadata should be None
    assert None == render_cell(
        timestamp_within_five_years,
        column="timestamp",
        table="mytable",
        database="mydatabase",
        datasette=Datasette(
            [], metadata={"plugins": {"datasette-render-timestamps": {"columns": []}}}
        ),
    )
