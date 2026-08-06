"""
Vector Configuration System

This file acts as the single source of truth for the entire application.
Any configurable value should be defined here.
"""

from dataclasses import dataclass
from pathlib import Path

# ==========================
# PROJECT PATHS
# ==========================

ROOT_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = ROOT_DIR / "assets"
DATABASE_DIR = ROOT_DIR / "database"
LOG_DIR = ROOT_DIR / "logs"
MODEL_DIR = ROOT_DIR / "models"
PLUGIN_DIR = ROOT_DIR / "plugins"


# Automatically create folders if they don't exist
for directory in (
    DATABASE_DIR,
    LOG_DIR,
    MODEL_DIR,
    PLUGIN_DIR,
):
    directory.mkdir(exist_ok=True)


# ==========================
# VECTOR SETTINGS
# ==========================


@dataclass(frozen=True)
class VectorConfig:
    """Global configuration for Vector."""

    name: str = "Vector"
    version: str = "2.0.0"

    wake_word: str = "hey vector"

    ai_model: str = "qwen2.5:3b"

    voice: str = "male"

    language: str = "en"

    debug: bool = True


config = VectorConfig()
