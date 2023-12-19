import asyncio
from aiopath import AsyncPath
import time
import os
from typing import Tuple, Dict, Any, Optional, List

from airflow.triggers.base import BaseTrigger, TriggerEvent
from airflow.utils import timezone

class FileCheckTrigger(BaseTrigger):
    def __init__(self, file_path: str, time_between_pokes: int = 5):
        """
        :param file_path: file path to check existence
        :param time_between_pokes: how many SECONDS should we wait between checks of the log file & SACCT
        """
        super().__init__()
        self.file_path = file_path
        self.time_between_pokes = time_between_pokes

    def serialize(self) -> Tuple[str, Dict[str, Any]]:
        return ("rxrx.triggers.foobar_trigger.FileCheckTrigger", {"file_path": self.file_path, "time_between_pokes": self.time_between_pokes})

    async def run(self):
        self.log.info(f"Setting up trigger with path {self.file_path}")
        path = AsyncPath(self.file_path)
        print("trigger going to sleep")
        while True:
            await asyncio.sleep(self.time_between_pokes)
            print("trigger awake")
            # very naughty blocking call for sanity checking:
            self.log.info(f'Currently in /tmp: {os.listdir("/tmp/")}')
            if await path.exists():
                self.log.info(f"Found file {path}, yielding")
                yield TriggerEvent(self.file_path)
            else:
                self.log.info("logging no file found, sleeping again")