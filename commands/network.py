"""
Network-related commands for Vector.
"""

import socket
import subprocess


def get_wifi_status() -> str:
    """Return the current Wi-Fi connection status."""

    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            check=False,
        )

        output = result.stdout

        if not output:
            return "Wi-Fi information is unavailable."

        state = None
        ssid = None

        for line in output.splitlines():
            line = line.strip()

            if line.startswith("State"):
                state = line.split(":", 1)[1].strip()

            elif line.startswith("SSID") and not line.startswith("BSSID"):
                ssid = line.split(":", 1)[1].strip()

        if state == "connected" and ssid:
            return f"Connected to Wi-Fi network {ssid}."

        if state:
            return f"Wi-Fi status: {state}."

        return "I couldn't determine the Wi-Fi status."

    except Exception:
        return "I couldn't access Wi-Fi information."


def check_internet() -> str:
    """Check whether the computer can reach the internet."""

    try:
        socket.create_connection(
            ("1.1.1.1", 53),
            timeout=2,
        )

        return "Internet connection is active."

    except OSError:
        return "There is no active internet connection."
