from loguru import logger
import sys


def handle_exception(exc_type, exc_value, exc_traceback) -> None:
    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception
