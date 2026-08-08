"""
Main Vector assistant.
"""

from loguru import logger

from commands.browser import open_youtube
from commands.system import show_time
from config.settings import config
from core.router import CommandRouter


class Assistant:
    """Main Vector assistant."""

    def __init__(self):
        self.router = CommandRouter()

        self._register_commands()

        logger.info(f"{config.name} {config.version} initialized.")

    def _register_commands(self) -> None:
        """Register all built-in Vector commands."""

        self.router.register(
            name="open_youtube",
            handler=open_youtube,
            description="Open YouTube",
        )
        self.router.register(
            name="show_time",
            handler=show_time,
            description="Show the current time",
        )

    def start(self) -> None:
        """Start Vector."""

        logger.info("Vector started.")

        print()
        print("=" * 50)
        print(f"{config.name} v{config.version}")
        print("AI Operating System")
        print("=" * 50)
        print()

        print("Available commands:")

        for command in self.router.list_commands():
            print(f"  - {command}")
