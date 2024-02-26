from sqlalchemy import exc
import pandas as pd
from loaders import RawLoader
from logger import Logger
from cfg import paths_dict, delimiter, SOURCE_PATH

log = Logger()


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

            log.error(f"Error loading data {name}: {e}")

        except Exception as e:

            log.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    run_load()
