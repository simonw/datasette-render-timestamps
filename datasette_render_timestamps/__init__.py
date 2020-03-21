import datetime
from datasette import hookimpl

min_timestamp = int(
    datetime.datetime.timestamp(
        (datetime.datetime.utcnow() - datetime.timedelta(days=5 * 365))
    )
)
max_timestamp = int(
    datetime.datetime.timestamp(
        (datetime.datetime.utcnow() + datetime.timedelta(days=5 * 365))
    )
)
default_format = "%B %d, %Y - %H:%M:%S UTC"


@hookimpl()
def render_cell(value, column, table, database, datasette):
    config = (
        datasette.plugin_config(
            "datasette-render-timestamps", database=database, table=table
        )
        or {}
    )
    if "format" not in config:
        config["format"] = default_format
    if not isinstance(value, int):
        return None
    # Is it within the range we care about?
    if not (min_timestamp < value < max_timestamp):
        return None
    dt = datetime.datetime.utcfromtimestamp(value)
    return dt.strftime(config["format"])
