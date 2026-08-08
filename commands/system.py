"""
System-related commands for Vector.
"""

from datetime import datetime

import psutil


def show_time() -> str:
    """Return the current system time."""

    current_time = datetime.now().strftime("%I:%M %p")

    return f"The current time is {current_time}."


def show_date() -> str:
    """Return the current date."""

    current_date = datetime.now().strftime("%A, %d %B %Y")

    return f"Today is {current_date}."


def show_battery() -> str:
    """Return battery percentage and charging status."""

    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is unavailable."

    percentage = battery.percent

    if battery.power_plugged:
        return f"Battery is at {percentage:.0f}% and charging."

    return f"Battery is at {percentage:.0f}%."


def show_cpu_usage() -> str:
    """Return current CPU usage."""

    usage = psutil.cpu_percent(interval=1)

    return f"CPU usage is {usage:.0f}%."


def show_memory_usage() -> str:
    """Return current RAM usage."""

    memory = psutil.virtual_memory()

    used = memory.percent

    return f"Memory usage is {used:.0f}%."


def show_system_status() -> str:
    """Return a basic system status report."""

    battery = psutil.sensors_battery()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    if battery is None:
        battery_info = "Battery unavailable"
    else:
        battery_info = f"{battery.percent:.0f}%"

    return f"CPU: {cpu:.0f}%, RAM: {memory:.0f}%, Battery: {battery_info}"
