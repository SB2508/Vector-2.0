"""
Main Vector assistant.
"""

from loguru import logger
from commands.power import lock_computer
from commands.apps import launch_application
from core.memory import Memory
from commands.audio import (
    get_volume,
    toggle_mute,
    volume_down,
    volume_up,
)
from commands.brightness import (
    brightness_down,
    brightness_up,
    get_brightness,
)
from commands.browser import (
    open_chatgpt,
    open_docs,
    open_drive,
    open_github,
    open_gmail,
    open_google,
    open_leetcode,
    open_linkedin,
    open_maps,
    open_netflix,
    open_stackoverflow,
    open_whatsapp,
    open_youtube,
)
from commands.network import (
    check_internet,
    get_wifi_status,
)
from commands.power import lock_computer
from commands.system import (
    show_battery,
    show_cpu_usage,
    show_date,
    show_memory_usage,
    show_system_status,
    show_time,
)
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
        self.memory = Memory()
        logger.info(f"{config.name} {config.version} initialized.")

    def _register_commands(self) -> None:
        """Register all built-in Vector commands."""
       
        self.router.register(
            name="open_youtube",
            handler=open_youtube,
            description="Open YouTube",
        )

        self.router.register(
            name="open_google",
            handler=open_google,
            description="Open Google",
        )

        self.router.register(
            name="open_gmail",
            handler=open_gmail,
            description="Open Gmail",
        )

        self.router.register(
            name="open_github",
            handler=open_github,
            description="Open GitHub",
        )

        self.router.register(
            name="open_linkedin",
            handler=open_linkedin,
            description="Open LinkedIn",
        )

        self.router.register(
            name="open_whatsapp",
            handler=open_whatsapp,
            description="Open WhatsApp Web",
        )
        self.router.register(
            name="launch_vscode",
            handler=lambda: launch_application("vs code"),
            description="Open Visual Studio Code",
        )
        self.router.register(
            name="open_chatgpt",
            handler=open_chatgpt,
            description="Open ChatGPT",
        )

        self.router.register(
            name="open_drive",
            handler=open_drive,
            description="Open Google Drive",
        )

        self.router.register(
            name="open_docs",
            handler=open_docs,
            description="Open Google Docs",
        )

        self.router.register(
            name="open_maps",
            handler=open_maps,
            description="Open Google Maps",
        )

        self.router.register(
            name="open_netflix",
            handler=open_netflix,
            description="Open Netflix",
        )

        self.router.register(
            name="open_stackoverflow",
            handler=open_stackoverflow,
            description="Open Stack Overflow",
        )
        self.router.register(
            name="open_leetcode",
            handler=open_leetcode,
            description="Open Leetcode",
        )
        self.router.register(
            name="show_time",
            handler=show_time,
            description="Show the current time",
        )
        self.router.register(
            name="show_date",
            handler=show_date,
            description="Show the current date",
        )

        self.router.register(
            name="show_battery",
            handler=show_battery,
            description="Show battery percentage",
        )

        self.router.register(
            name="show_cpu_usage",
            handler=show_cpu_usage,
            description="Show CPU usage",
        )

        self.router.register(
            name="show_memory_usage",
            handler=show_memory_usage,
            description="Show RAM usage",
        )

        self.router.register(
            name="show_system_status",
            handler=show_system_status,
            description="Show system status",
        )
        self.router.register(
            name="get_volume",
            handler=get_volume,
            description="Show the current volume",
        )

        self.router.register(
            name="volume_up",
            handler=volume_up,
            description="Increase the volume",
        )

        self.router.register(
            name="volume_down",
            handler=volume_down,
            description="Decrease the volume",
        )

        self.router.register(
            name="toggle_mute",
            handler=toggle_mute,
            description="Mute or unmute the system",
        )

        self.router.register(
            name="get_brightness",
            handler=get_brightness,
            description="Show screen brightness",
        )

        self.router.register(
            name="brightness_up",
            handler=brightness_up,
            description="Increase screen brightness",
        )

        self.router.register(
            name="brightness_down",
            handler=brightness_down,
            description="Decrease screen brightness",
        )
        self.router.register(
            name="get_wifi_status",
            handler=get_wifi_status,
            description="Show Wi-Fi connection status",
        )

        self.router.register(
            name="check_internet",
            handler=check_internet,
            description="Check internet connection",
        )
        self.router.register(
            name="launch_notepad",
            handler=lambda: launch_application("notepad"),
            description="Open Notepad",
        )

        self.router.register(
            name="launch_calculator",
            handler=lambda: launch_application("calculator"),
            description="Open Calculator",
        )

        self.router.register(
            name="launch_explorer",
            handler=lambda: launch_application("file explorer"),
            description="Open File Explorer",
        )
        self.router.register(
            name="lock_computer",
            handler=lock_computer,       
            description="Lock the computer",
        )
        self.router.register(
            name="remember",
            handler=lambda: self.remember(
                "Vector memory test"
            ),
            description="Store something in memory",
        )

        self.router.register(
            name="show_memories",
            handler=self.show_memories,
            description="Show stored memories",
        )
        self.router.register(
            name="search_memory",
            handler=lambda: self.search_memory("python"),
            description="Search Vector's memory",
        )

    def process_input(self, user_input: str) -> str:
        """Process a user's text input."""

        user_input = user_input.strip()

        # Memory detection
        memory_prefixes = [
            "remember that ",
            "remember ",
        ]

        for prefix in memory_prefixes:
            if user_input.lower().startswith(prefix):
                memory_text = user_input[len(prefix):].strip()

                if not memory_text:
                    return "What would you like me to remember?"

                self.memory.remember(memory_text)

                return "I'll remember that."

        # Normal Vector processing
        intent = self.intent_detector.detect(user_input)

        if intent is None:
            return self.brain.think(user_input)

        result = self.router.execute(intent)

        return result
    def search_memory(self, query: str) -> str:
        """Search Vector's stored memories."""

        matches = self.memory.search(query)

        if not matches:
            return "I don't remember anything about that."

        return "I remember: " + " | ".join(matches)
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
    def remember(self, text: str) -> str:
        """Store something in Vector's memory."""

        if not text.strip():
            return "What would you like me to remember?"

        self.memory.remember(text.strip())

        return "I'll remember that."


    def show_memories(self) -> str:
        """Return Vector's stored memories."""

        memories = self.memory.get_all()

        if not memories:
            return "I don't have any memories yet."

        lines = [
            f"{index}. {memory['text']}"
            for index, memory in enumerate(memories, start=1)
        ]

        return "Here's what I remember:\n" + "\n".join(lines)