"""
Main Vector assistant.
"""

from loguru import logger

from commands.browser import open_youtube
from commands.system import show_time
from config.settings import config
from core.brain import LocalBrain
from core.intent import IntentDetector
from core.router import CommandRouter


class Assistant:
    """Main Vector assistant."""

    def __init__(self):
        self.router = CommandRouter()
        self.intent_detector = IntentDetector()
        self.brain = LocalBrain()
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

    def process_input(self, user_input: str) -> str:
        """Process a user's text input."""

        intent = self.intent_detector.detect(user_input)

        if intent is None:
            return self.brain.think(user_input)

        result = self.router.execute(intent)

        return result

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
