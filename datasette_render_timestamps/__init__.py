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
# output format
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

    columns = config.get("columns")
    if columns is None:
        # autodetect recent unix timestamps
        if isinstance(value, int) and (min_timestamp < value < max_timestamp):
            dt = datetime.datetime.utcfromtimestamp(value)
        else:
            return None
    else:
        # only proceed if the column is mentioned explicitly
        if column not in columns:
            return None

        if isinstance(value, int):
            dt = datetime.datetime.utcfromtimestamp(value)
        # only parse strings with an explicit read format
        elif isinstance(value, str) and "read_format" in config:
            dt = datetime.datetime.strptime(value, config["read_format"])
        else:
            return None

    return dt.strftime(config["format"])
