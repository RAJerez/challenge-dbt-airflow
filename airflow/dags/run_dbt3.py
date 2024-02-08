from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG("run_dbt3",
    start_date=datetime(2024, 2, 7),
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
    ) as dag:
    
    t1 = BashOperator(
        task_id='virtualenv', bash_command='poetry shell', dag=dag)

    t2 = BashOperator(
        task_id='run_dbt', bash_command='dbt run', dag=dag)

t1 >> t2   # This is how we set dependency among two tasks