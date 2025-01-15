import logging as log
from .config import LOG_PATH


db_logger = log.getLogger(__name__)
db_logger.setLevel(level=log.INFO)

if not db_logger.handlers:
    app_handler = log.FileHandler(LOG_PATH, mode="a")
    app_formater = log.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    app_handler.setFormatter(app_formater)
    db_logger.addHandler(app_handler)
