import logging

def get_logger():
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler("logs/tests.log")

    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)

    return logger