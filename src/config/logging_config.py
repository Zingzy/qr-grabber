import os
import sys
from loguru import logger

# Configure log directory
LOG_DIR: str = os.path.join(os.path.expanduser("~"), ".qr_grabber", "logs")
os.makedirs(LOG_DIR, exist_ok=True)


def setup_logging():
    """Set up comprehensive logging configuration"""
    # Remove default logger
    logger.remove()

    # Console logging
    if sys.stdout is not None:
        logger.add(
            sys.stderr,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            level="INFO",
        )

    # File logging with rotation
    logger.add(
        os.path.join(LOG_DIR, "qr_grabber_{time}.log"),
        rotation="10 MB",  # Rotate when file reaches 10 MB
        retention="10 days",  # Keep logs for 10 days
        compression="zip",  # Compress old log files
        level="DEBUG",  # Capture debug and above
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        diagnose=True,  # Add more context to tracebacks
    )

    return logger
