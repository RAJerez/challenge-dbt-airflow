from pathlib import Path

BASE_FILE_DIR = Path("/tmp")  # file storage path
ROOT_DIR = Path().resolve().parent  # project root path
SQL_DIR = ROOT_DIR / "data-challenge-dbt/sql"  # path with sql files
SETTINGS_DIR = ROOT_DIR / "data-challenge-dbt"

# Table names
CINE_TABLE_NAME = "raw_cine"
MUSEO_TABLE_NAME = "raw_museo"
BIBLIOTECA_TABLE_NAME = "raw_biblioteca"

# List with table names
TABLE_NAMES = [
    CINE_TABLE_NAME,
    MUSEO_TABLE_NAME,
    BIBLIOTECA_TABLE_NAME,
]
