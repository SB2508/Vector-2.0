"""
System-related commands for Vector.
"""

import datetime


def show_time() -> str:
    """Return the current system time."""

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    return f"The current time is {current_time}."
