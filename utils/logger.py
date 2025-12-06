import logging, os
from datetime import datetime

LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger