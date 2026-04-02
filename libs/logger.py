import logging

"""
Usage:

import logging
from logger import get_logger

logger = get_logger(__name__)
(optional) logger = get_logger(__name__, level=logging.DEBUG)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
"""


class CustomFormatter(logging.Formatter):
    cyan = "\x1b[36;20m"
    grey = "\x1b[38;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s.%(msecs)03d [%(name)s] %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: cyan + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, self.FORMATS[logging.INFO])
        date_fmt = self.DATE_FORMAT
        formatter = logging.Formatter(log_fmt, date_fmt)
        return formatter.format(record)


def get_logger(name, level=logging.INFO):
    """Logger for use in console."""
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(level)
        handler = logging.StreamHandler()
        handler.setFormatter(CustomFormatter())
        logger.addHandler(handler)

    return logger
