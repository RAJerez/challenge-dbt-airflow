from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': 'rodrigoagustin23@gmail.com',
    'email_on_retry': 'rodrigoagustin23@gmail.com',
    'retries': 1,
}

dag = DAG(
    'run_dbt2',
    default_args = default_args,
    description = 'Run the commands $poetry shell and $dbt run',
    schedule_interval = '@daily',
    start_date = days_ago(1),
    catchup = False
)

def run_dbt():
    import os
    os.system("poetry shell && dbt run")

run_dbt_virtualenv = PythonOperator(
    task_id = 'ejecutar_dbt_run_virtualenv',
    python_callable = run_dbt,
    dag = dag
)

run_dbt_virtualenv