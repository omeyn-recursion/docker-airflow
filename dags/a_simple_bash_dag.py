import os
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.bash import BashOperator

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
    "a_simple_bash_dag",
    default_args=default_args,
    catchup=False,
    schedule_interval=None,
) as dag:
    sync_buckets = BashOperator(
        task_id="a_simple_bash_dag",
        bash_command=f"ls /tmp/",
    )
