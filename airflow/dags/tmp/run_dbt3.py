from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

DBT_PROJECT_DIR="../opt/dbt"
DBT_PROFILES_DIR="../opt/dbt"

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
    
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}",
        dag=dag)

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=f"dbt testrun --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}",
        dag=dag)

dbt_run >> dbt_test