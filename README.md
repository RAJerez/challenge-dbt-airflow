# Data Challenge - DBT

Este proyecto se centra en el procesamiento de datos del desafío de data "data-challenge", esta vez aplicando modelos DBT.

Se consumirán datos desde 3 tablas con información en crudo sobre bibliotecas, museos y salas de cines argentinos en una base de datos Postgres.

## Procesamiento de datos
El procesamiento de datos permitirá a nuestro proyecto transformar los datos de los
archivos fuente en la información que va a nutrir la base de datos. Para esto, el
proyecto deberá:

- Normalizar toda la información de museos, cines y bibliotecas y generar tablas que cuenten con las siguientes columnas.
    - cod_localidad
    - id_provincia
    - id_departamento
    - categoría
    - provincia
    - localidad
    - nombre
    - domicilio
    - código postal
    - número de teléfono
    - mail
    - web

- Procesar los datos conjuntos para poder generar una tabla con la siguiente información:
    - Cantidad de registros totales por categoría
    - Cantidad de registros totales por fuente
    - Cantidad de registros por provincia y categoría


- Procesar la información de cines para poder crear una tabla que contenga:
    - Provincia
    - Cantidad de pantallas
    - Cantidad de butacas
    - Cantidad de espacios INCAA


## Prerequisitos
#### Poetry
Utilizé Poetry para un mejor manejo de dependecias y también para crear mi entorno virtual.

Instalar poetry desde pipx y la instalación se realizara aislada del entorno global
```bash
pipx install poetry
```

Para instalar las dependencias necesarias descriptas en pyproyect.toml
```bash
poetry install
```

Automaticamente se creara un entorno virtual al cual puede acceder
```bash
poetry shell
```

#### Option without Poetry
En caso de no usar poetry puede instalar las dependencias a traves de requirements.txt
El proyecto se realizó con Python 3.10
```bash
python3 -m virtualenv venv
source venv/bin/activate
pip install -r 'requirements.txt'
```

## Creation of the database, tables and execution of data pipeline
Raise container with Postgres database:
```bash
sudo docker compose up -d
```

You can access the database through the bash terminal
```bash
docker exec -it postgres psql -U postgres -d data-challenge-dbt
```

Loading raw data into database
El siguiente script realiza la conexión con la base de datos y realiza la carga.
```bash
python3 main.py
```

Run DBT models:
```bash
dbt run
```


## Airflow Installation


```bash
mkdir airflow
cd airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/<version>/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins ./config
chmod -R 777 ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
chmod -R 755 .env
docker compose up airflow-init
docker compose up
```