"""
Main Assistant class.
"""

from loguru import logger

from config.settings import config


class Assistant:
    """Main Vector assistant."""

    def __init__(self):
        logger.info(f"{config.name} {config.version} is starting...")

    def start(self):
        logger.info("System initialized successfully.")

        print()
        print("=" * 50)
        print(f"{config.name} v{config.version}")
        print("AI Operating System")
        print("=" * 50)
        print()
