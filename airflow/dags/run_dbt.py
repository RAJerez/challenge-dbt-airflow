from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id = "dbt_run_dag",
    start_date = datetime(2024, 2, 7),
    schedule_interval = "@daily",
) as dag:
    
    dbt_run_task = BashOperator(
        task_id = "dbt_run",
        bash_command = "dbt run",
    )

dbt_run_task