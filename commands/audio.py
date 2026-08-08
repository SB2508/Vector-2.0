"""
Audio control commands for Vector on Windows.
"""

from pycaw.pycaw import AudioUtilities


def _get_volume_interface():
    """Return the Windows master-volume interface."""

    device = AudioUtilities.GetSpeakers()

    return device.EndpointVolume


def get_volume() -> str:
    """Return the current master volume."""

    volume = _get_volume_interface()

    level = volume.GetMasterVolumeLevelScalar() * 100

    return f"Volume is at {level:.0f}%."


def set_volume(level: int) -> str:
    """Set the master volume to a percentage."""

    if not 0 <= level <= 100:
        return "Volume must be between 0 and 100 percent."

    volume = _get_volume_interface()

    volume.SetMasterVolumeLevelScalar(level / 100, None)

    return f"Volume set to {level}%."


def volume_up() -> str:
    """Increase the master volume by 10%."""

    volume = _get_volume_interface()

    current = volume.GetMasterVolumeLevelScalar() * 100
    new_level = min(current + 10, 100)

    volume.SetMasterVolumeLevelScalar(new_level / 100, None)

    return f"Volume increased to {new_level:.0f}%."


def volume_down() -> str:
    """Decrease the master volume by 10%."""

    volume = _get_volume_interface()

    current = volume.GetMasterVolumeLevelScalar() * 100
    new_level = max(current - 10, 0)

    volume.SetMasterVolumeLevelScalar(new_level / 100, None)

    return f"Volume decreased to {new_level:.0f}%."


def toggle_mute() -> str:
    """Toggle system mute."""

    volume = _get_volume_interface()

    muted = volume.GetMute()

    volume.SetMute(not muted, None)

    if muted:
        return "Volume unmuted."

    return "Volume muted."
