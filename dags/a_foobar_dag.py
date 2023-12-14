import os
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from rxrx.operators.foobar_operator import FileCheckOperator

default_args = {
    "owner": "Airflow",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "a_foobar_dag",
    default_args=default_args,
    catchup=False,
    schedule_interval=None,
) as dag:
    found_file = FileCheckOperator(file_path="/tmp/foo.bar", task_id="a_foobar_bash_dag",)
