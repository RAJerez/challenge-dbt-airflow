import os
import pandas as pd
from logger import Logger


log = Logger()


def csv_to_parquet(source_path, destination_path):
    try:

        if not os.path.exists(source_path):
            log.error(f"Source file '{source_path}' not found.")
            return

        df = pd.read_csv(source_path)
        df.to_parquet(destination_path, index=False)

        log.info(
            f"CSV file '{source_path}' converted to Parquet file '{destination_path}' successfully."
        )
    except Exception as e:
        log.error(f"Error occurred: {e}")
