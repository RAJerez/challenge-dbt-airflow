# Data Loading and Processing Project with Airflow, Minio, and DBT

This project aims to load data from CSV files into a Minio storage bucket, followed by processing this data into different layers using DBT, all managed through Airflow. Below are the main components and their functionality in this workflow.

## Main Components:
### 1. Python Script for Minio Upload

The Python script is responsible for uploading CSV files to a Minio storage bucket. The files are organized into bronze, silver, and gold folders depending on their processing status.

### 2. Airflow DAGs

Airflow is used to orchestrate the entire workflow. DAGs (Directed Acyclic Graphs) are defined to manage the execution of each step, from data loading to processing with DBT.


### 3. DBT (Data Build Tool)

DBT is used to transform the data into different layers: bronze, silver, and gold. Each layer represents a level of data processing and refinement, from the raw stage to the final and optimized version.

### 4. Minio Storage

Minio is an open-source object storage system. It is used to store the CSV files that will be loaded and processed in the workflow.


## Project Structure
```bash
minio-dbt-airflow/
├── airflow/
│   ├── config
│   ├── dags
│   ├── docker
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── logs  
│   ├── plugins
│
├── dbt/
│   ├── dbt_airflow
│   │   ├── models
│   │   │   ├── bronze
│   │   │   ├── silver
│   │   │   └── gold
│   ├── dbt_packages
│   ├── dbt_project.yml
│   ├── logs
│   └── profiles.yml
│
├── minio/
│   └── docker
│       ├── Dockerfile
│       └── requirements.txt
│
├── cfg.py
├── main.py
├── raw_data
├── docker-compose.yaml
└── README.md



```

## Status: Under Development

Please note that this project is currently under active development. Some features may not be fully implemented, and changes are expected. Feel free to contribute or provide feedback to help improve the project.




## Airflow Installation

To install Apache Airflow, follow these steps:


1. Create a directory for Airflow:
```bash
mkdir airflow
cd airflow
```


2. Download the Docker Compose file for Airflow. Replace `<version>` with the desired version of Airflow:
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/<version>/docker-compose.yaml'
```


3. Create necessary directories for Airflow:
```bash
mkdir -p ./dags ./logs ./plugins ./config
chmod -R 777 ./dags ./logs ./plugins ./config
```


4. Set permissions for the `env` file:
```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
chmod -R 755 .env
```


5. Initialize Airflow metadata db:
```bash
docker compose up airflow-init
```

6. Start Airflow services:
```bash
docker compose up
```