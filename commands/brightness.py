"""
Display brightness commands for Vector.
"""

import screen_brightness_control as sbc


def get_brightness() -> str:
    """Return the current screen brightness."""

    try:
        brightness = sbc.get_brightness()

        if not brightness:
            return "Brightness information is unavailable."

        return f"Brightness is at {brightness[0]}%."

    except Exception:
        return "I couldn't access the display brightness."


def set_brightness(level: int) -> str:
    """Set screen brightness."""

    if not 0 <= level <= 100:
        return "Brightness must be between 0 and 100 percent."

    try:
        sbc.set_brightness(level)

        return f"Brightness set to {level}%."

    except Exception:
        return "I couldn't change the display brightness."


def brightness_up() -> str:
    """Increase screen brightness by 10%."""

    try:
        current = sbc.get_brightness()[0]
        new_level = min(current + 10, 100)

        sbc.set_brightness(new_level)

        return f"Brightness increased to {new_level}%."

    except Exception:
        return "I couldn't increase the display brightness."


def brightness_down() -> str:
    """Decrease screen brightness by 10%."""

    try:
        current = sbc.get_brightness()[0]
        new_level = max(current - 10, 0)

        sbc.set_brightness(new_level)

        return f"Brightness decreased to {new_level}%."

    except Exception:
        return "I couldn't decrease the display brightness."
