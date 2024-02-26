import os
import pandas as pd
from logger import Logger

# Crear instancia de Logger
log = Logger()

def csv_to_parquet(source_path, destination_path):
    try:
        # Verificar si el archivo de origen existe
        if not os.path.exists(source_path):
            log.error(f"Source file '{source_path}' not found.")
            return
        
        # Leer el archivo CSV y convertirlo a Parquet
        df = pd.read_csv(source_path)
        df.to_parquet(destination_path, index=False)
        
        # Registrar mensaje de éxito
        log.info(f"CSV file '{source_path}' converted to Parquet file '{destination_path}' successfully.")
    except Exception as e:
        # Manejar cualquier error que ocurra durante el proceso
        log.error(f"Error occurred: {e}")




# Ejemplo de uso:
# source_csv = "ruta/a/tu/archivo.csv"
# destination_parquet = "ruta/a/destino/archivo.parquet"

# csv_to_parquet(source_csv, destination_parquet)