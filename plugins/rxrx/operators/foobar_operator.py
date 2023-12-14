import os
from typing import Dict, Optional, Sequence, Any, List
import dateutil.parser

from airflow.exceptions import AirflowException, AirflowSkipException
from airflow.models import Variable
from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context

from rxrx.triggers.foobar_trigger import FileCheckTrigger

class FileCheckOperator(BaseOperator):
    
    def __init__(self, file_path: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.file_path = file_path

    def execute(self, context: Context):
        self.log.info("Foobar being executed")
        print("print line - foobar being executed")
        self.defer(trigger=FileCheckTrigger(file_path=self.file_path, time_between_pokes=1), method_name="found_file")

        return True
    
    def found_file(self, context):
        print("print line - found file, foobar exiting")
        self.log.info("Found file. Final method called!")