"""
Browser-related commands for Vector.
"""

import webbrowser


def open_url(url: str) -> str:
    """Open a URL in the default browser."""

    webbrowser.open(url)

    return f"Opening {url}"


def open_youtube() -> str:
    """Open YouTube."""

    return open_url("https://www.youtube.com")


def open_google() -> str:
    """Open Google."""

    return open_url("https://www.google.com")


def open_gmail() -> str:
    """Open Gmail."""

    return open_url("https://mail.google.com")


def open_github() -> str:
    """Open GitHub."""

    return open_url("https://github.com")


def open_linkedin() -> str:
    """Open LinkedIn."""

    return open_url("https://www.linkedin.com")


def open_whatsapp() -> str:
    """Open WhatsApp Web."""

    return open_url("https://web.whatsapp.com")


def open_chatgpt() -> str:
    """Open ChatGPT."""

    return open_url("https://chatgpt.com")


def open_drive() -> str:
    """Open Google Drive."""

    return open_url("https://drive.google.com")


def open_docs() -> str:
    """Open Google Docs."""

    return open_url("https://docs.google.com")


def open_maps() -> str:
    """Open Google Maps."""

    return open_url("https://maps.google.com")


def open_netflix() -> str:
    """Open Netflix."""

    return open_url("https://www.netflix.com")


def open_stackoverflow() -> str:
    """Open Stack Overflow."""

    return open_url("https://stackoverflow.com")


def open_leetcode() -> str:
    """Open Stack Overflow."""

    return open_url("https://leetcode.com")
