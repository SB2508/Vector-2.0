"""
Entry point for Vector.
"""

# Import initializes the logging configuration.

from core.assistant import Assistant


def main():
    assistant = Assistant()
    assistant.start()


if __name__ == "__main__":
    main()
