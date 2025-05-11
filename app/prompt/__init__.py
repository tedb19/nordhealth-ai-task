from pathlib import Path


def load_prompt(name: str) -> str:
    path = Path(__file__).parent / f"{name}.txt"
    return path.read_text(encoding="utf-8").strip()
