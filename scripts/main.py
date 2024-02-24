# This script load the raw data into database
from sqlalchemy import exc
import pandas as pd
from loaders import RawLoader
import logging
from cfg import paths_dict, delimiter, SOURCE_PATH


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s",
    filename="registry.log",
    filemode="a",
)

log = logging.getLogger()


def run_load():
    for name, file in paths_dict.items():
        file_path = SOURCE_PATH + file
        if name in delimiter:
            separator = ";"
        else:
            separator = ","
        log.debug(f"Loading {name}")

        try:
            RawLoader(name).load_table(file_path, separator)
            log.info(f"Data {name} loaded correctly")

        except exc.SQLAlchemyError as e:
            # SQLAlchemy Specific Errors
            log.error(f"Error loading data {name}: {e}")

        except Exception as e:
            # General exceptions
            log.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    run_load()
