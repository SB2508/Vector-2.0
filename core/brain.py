"""
Local AI brain for Vector.
"""

from ollama import chat


class LocalBrain:
    """Interface between Vector and the local Ollama model."""

    def __init__(self, model: str = "qwen3:4b"):
        self.model = model

    def think(self, prompt: str) -> str:
        """Send a prompt to the local AI model."""

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]
