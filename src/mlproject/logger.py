import logging
import os
from datetime import datetime

LOG_FILE = os.path.join(os.getcwd(), "logs", f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log") 
log_path = os.path.dirname(LOG_FILE)

os.makedirs(log_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("mlflow")
