"""
Application launching commands for Vector.
"""

import subprocess

APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "file explorer": "explorer.exe",
    "explorer": "explorer.exe",
    "vs code": "code",
}


def launch_application(name: str) -> str:
    """Launch a Windows application."""

    application = APPLICATIONS.get(name.lower().strip())

    if application is None:
        return f"I don't know how to open {name} yet."

    try:
        subprocess.Popen(
            application,
            shell=False,
        )

        return f"Opening {name}."

    except OSError:
        return f"I couldn't open {name}."
