from airflow import DAG
from airflow.operators.bash_operator import BashOperator
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

run_dbt_command = """
source /home/agustin/.cache/pypoetry/virtualenvs/dbt-airflow-5EcEiW5e-py3.10/bin/activate &&
dbt rub
"""

run_dbt_virtualenv = BashOperator(
    task_id = 'ejecutar_dbt_run_virtualenv',
    bash_command = run_dbt_command,
    dag = dag
)

run_dbt_virtualenv