"""
Logging configuration for Vector.
"""

from loguru import logger

from config.settings import LOG_DIR

LOG_FILE = LOG_DIR / "vector.log"

# Remove the default logger
logger.remove()

# Console logger
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    colorize=True,
)

# File logger
logger.add(
    LOG_FILE,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="DEBUG",
    enqueue=True,
)

logger.info("Logging system initialized.")
