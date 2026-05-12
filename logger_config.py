import logging
import os


LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    "app.log"
)


def setup_logger() -> logging.Logger:
    """
    Configure application logger.
    """

    logger = logging.getLogger(
        "analytics_logger"
    )

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler(
            LOG_FILE
        )

        formatter = logging.Formatter(
            (
                "%(asctime)s - "
                "%(levelname)s - "
                "%(name)s - "
                "%(message)s"
            )
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger


logger = setup_logger()