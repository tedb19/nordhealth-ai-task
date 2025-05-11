import json
from pathlib import Path


def load_json(path: Path) -> dict:
    with Path.open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with Path.open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
