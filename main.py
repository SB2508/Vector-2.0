"""
Entry point for Vector.
"""

from core.assistant import Assistant


def main():
    assistant = Assistant()

    print()
    print("=" * 50)
    print("Vector 2.0")
    print("AI Operating System")
    print("=" * 50)
    print()

    while True:
        user_input = input("You: ")

        if user_input.lower() in {"exit", "quit"}:
            print("Vector: Goodbye.")
            break

        response = assistant.process_input(user_input)

        print(f"Vector: {response}")


if __name__ == "__main__":
    main()
