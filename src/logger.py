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

