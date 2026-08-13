"""
Vector's local memory system.
"""

import json
from pathlib import Path


class Memory:
    """Simple persistent local memory for Vector."""

    def __init__(self, file_path="data/memory.json"):
        self.file_path = Path(file_path)

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.file_path.exists():
            self.file_path.write_text(
                "[]",
                encoding="utf-8",
            )

    def _load(self):
        """Load memories from disk."""

        try:
            return json.loads(self.file_path.read_text(encoding="utf-8"))

        except (json.JSONDecodeError, OSError):
            return []

    def _save(self, memories):
        """Save memories to disk."""

        self.file_path.write_text(
            json.dumps(
                memories,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    def remember(self, text):
        """Store a new memory."""

        memories = self._load()

        memories.append(
            {
                "text": text,
            }
        )

        self._save(memories)

    def get_all(self):
        """Return all stored memories."""

        return self._load()
    def search(self, query: str) -> list[str]:
        """Find memories containing words from the query."""

        query_words = set(
            query.lower().split()
        )

        memories = self._load()

        matches = []

        for memory in memories:
            text = memory.get("text", "")
            text_words = set(text.lower().split())

            if query_words & text_words:
                matches.append(text)

        return matches
    def clear(self):
        """Delete all stored memories."""

        self._save([])
if __name__ == "__main__":
    memory = Memory()

    print("All memories:")
    print(memory.get_all())

    print("\nSearch results:")
    print(memory.search("Python"))

