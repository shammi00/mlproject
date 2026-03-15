import logging
import os
from datetime import datetime

Log_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
Log_FILE_PATH = os.path.join(os.getcwd(),"logs",Log_FILE_NAME)
os.makedirs(os.path.dirname(Log_FILE_PATH),exist_ok=True)
logging.basicConfig(
    filename=Log_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

"""
The above code sets up a logging configuration for a Python application.
It creates a log file with a name based on the current date and time, and stores it in a "logs" directory within the current working directory.
The logging format includes the timestamp, line number, logger name, log level, and the log message.
The logging level is set to INFO, which means that all log messages at this level and above will be recorded in the log file.
This setup allows for organized and timestamped logging of events and errors in the application.
"""