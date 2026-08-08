"""
Windows power-management commands for Vector.
"""

import subprocess


def lock_computer() -> str:
    """Lock the Windows computer."""

    try:
        subprocess.run(
            ["rundll32.exe", "user32.dll,LockWorkStation"],
            check=False,
        )

        return "Computer locked."

    except OSError:
        return "I couldn't lock the computer."


def restart_computer() -> str:
    """Restart Windows."""

    try:
        subprocess.Popen(
            ["shutdown", "/r", "/t", "5"],
            shell=False,
        )

        return "Computer will restart in 5 seconds."

    except OSError:
        return "I couldn't restart the computer."


def shutdown_computer() -> str:
    """Shut down Windows."""

    try:
        subprocess.Popen(
            ["shutdown", "/s", "/t", "5"],
            shell=False,
        )

        return "Computer will shut down in 5 seconds."

    except OSError:
        return "I couldn't shut down the computer."


def cancel_shutdown() -> str:
    """Cancel a pending Windows shutdown or restart."""

    try:
        subprocess.Popen(
            ["shutdown", "/a"],
            shell=False,
        )

        return "Pending shutdown or restart cancelled."

    except OSError:
        return "I couldn't cancel the pending shutdown."
