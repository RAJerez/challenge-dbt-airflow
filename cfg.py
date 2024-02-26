from decouple import config

# I raise the variables from .env
POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
POSTGRES_HOST = config("POSTGRES_HOST")
POSTGRES_PORT = config("POSTGRES_PORT")
POSTGRES_DB = config("POSTGRES_DB")
SOURCE_PATH = config("SOURCE_PATH")
DB_CONNSTR = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

BUCKET = config("BUCKET")
ENDPOINT_URL = config("ENDPOINT_URL")
MINIO_ACCESS_KEY = config("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = config("MINIO_SECRET_KEY")

paths_dict = {
    "canal_venta": "CanalDeVenta.csv",
    "cliente": "Clientes.csv",
    "compra": "Compra.csv",
    "empleado": "Empleados.csv",
    "gasto": "Gasto.csv",
    "producto": "Productos.csv",
    "proveedor": "Proveedores.csv",
    "sucursal": "Sucursales.csv",
    "tipo_gasto": "TiposDeGasto.csv",
    "venta": "Venta.csv",
}

delimiter = ["cliente", "sucursal"]