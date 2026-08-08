"""
Command routing system for Vector.
"""

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    """Represents a command that Vector can execute."""

    name: str
    handler: Callable
    description: str


class CommandRouter:
    """Routes user requests to registered command handlers."""

    def __init__(self):
        self._commands: dict[str, Command] = {}

    def register(
        self,
        name: str,
        handler: Callable,
        description: str = "",
    ) -> None:
        """Register a new command."""

        command = Command(
            name=name,
            handler=handler,
            description=description,
        )

        self._commands[name] = command

    def execute(self, name: str, *args, **kwargs):
        """Execute a registered command."""

        command = self._commands.get(name)

        if command is None:
            raise ValueError(f"Unknown command: {name}")

        return command.handler(*args, **kwargs)

    def has_command(self, name: str) -> bool:
        """Check whether a command exists."""

        return name in self._commands

    def list_commands(self) -> list[str]:
        """Return all registered command names."""

        return list(self._commands.keys())
