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
