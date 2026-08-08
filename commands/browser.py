"""
Browser-related commands for Vector.
"""

import webbrowser


def open_youtube() -> str:
    """Open YouTube in the default browser."""

    webbrowser.open("https://www.youtube.com")

    return "YouTube opened."
