"""
Intent detection system for Vector.

This module converts natural-language requests into
known Vector command names.
"""


class IntentDetector:
    """Detect the intended Vector command from user input."""

    def __init__(self):
        self._intents = {
            "open_youtube": [
                "open youtube",
                "launch youtube",
                "start youtube",
                "go to youtube",
                "take me to youtube",
            ],
            "show_time": [
                "what time is it",
                "what's the time",
                "tell me the time",
                "show me the time",
                "current time",
            ],
            "open_google": [
                "open google",
                "launch google",
                "start google",
                "go to google",
            ],
            "open_gmail": [
                "open gmail",
                "launch gmail",
                "open my email",
                "open email",
            ],
            "open_github": [
                "open github",
                "launch github",
                "go to github",
            ],
            "open_linkedin": [
                "open linkedin",
                "launch linkedin",
                "go to linkedin",
            ],
            "open_whatsapp": [
                "open whatsapp",
                "launch whatsapp",
                "open whatsapp web",
            ],
            "open_chatgpt": [
                "open chatgpt",
                "launch chatgpt",
                "go to chatgpt",
            ],
            "open_drive": [
                "open google drive",
                "open drive",
                "launch drive",
            ],
            "open_docs": [
                "open google docs",
                "open docs",
                "launch docs",
            ],
            "open_maps": [
                "open google maps",
                "open maps",
                "launch maps",
            ],
            "open_netflix": [
                "open netflix",
                "launch netflix",
                "go to netflix",
            ],
            "open_stackoverflow": [
                "open stack overflow",
                "open stackoverflow",
                "open stack",
                "launch stack overflow",
            ],
            "open_leetcode": [
                "open leetcode",
                "open leet",
                "let me code some questions",
            ],
            "show_date": [
                "what is today's date",
                "what's today's date",
                "what is the date",
                "tell me the date",
                "show me the date",
            ],
            "show_battery": [
                "what is my battery",
                "battery percentage",
                "battery level",
                "how much battery",
                "check battery",
            ],
            "show_cpu_usage": [
                "cpu usage",
                "processor usage",
                "how much cpu",
                "check cpu",
            ],
            "show_memory_usage": [
                "memory usage",
                "ram usage",
                "how much ram",
                "check ram",
            ],
            "show_system_status": [
                "system status",
                "system information",
                "computer status",
                "check my computer",
            ],
            "get_volume": [
                "what is the volume",
                "volume level",
                "check volume",
                "how loud is it",
            ],
            "volume_up": [
                "increase volume",
                "volume up",
                "turn volume up",
                "make it louder",
            ],
            "volume_down": [
                "decrease volume",
                "volume down",
                "turn volume down",
                "make it quieter",
            ],
            "toggle_mute": [
                "mute",
                "mute volume",
                "unmute",
                "unmute volume",
            ],
            "get_brightness": [
                "what is the brightness",
                "brightness level",
                "check brightness",
                "how bright is the screen",
            ],
            "brightness_up": [
                "increase brightness",
                "brightness up",
                "turn brightness up",
                "make the screen brighter",
            ],
            "brightness_down": [
                "decrease brightness",
                "reduce brightness",
                "brightness down",
                "turn brightness down",
                "make the screen darker",
            ],
            "get_wifi_status": [
                "wifi status",
                "check wifi",
                "what wifi am i connected to",
                "what wifi is connected",
                "show wifi",
            ],
            "launch_vscode": [
                "open vs code",
                "open visual studio code",
                "launch vs code",
                "launch visual studio code",
                "start vs code",
                "lets code",
            ],
            "check_internet": [
                "internet status",
                "check internet",
                "am i connected to the internet",
                "is the internet working",
                "do i have internet",
            ],
            "launch_notepad": [
                "open notepad",
                "launch notepad",
                "start notepad",
                "note something",
            ],
            "launch_calculator": [
                "open calculator",
                "launch calculator",
                "start calculator",
                "calculate something",
            ],
            "launch_explorer": [
                "open file explorer",
                "open explorer",
                "launch file explorer",
            ],
            "lock_computer": [
                "lock my computer",
                "lock the computer",
                "lock pc",
                "lock my pc",
            ],
        }

    def detect(self, text: str) -> str | None:
        """
        Detect an intent from user input.

        Returns:
            The command name if an intent is detected,
            otherwise None.
        """

        normalized_text = text.lower().strip()

        for command_name, phrases in self._intents.items():
            for phrase in phrases:
                if phrase in normalized_text:
                    return command_name

        return None
