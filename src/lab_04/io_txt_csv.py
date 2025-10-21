import csv
from pathlib import Path
from typing import Dict, List, Tuple


def read_text(path: Path) -> str:
    """Читает текст из .txt файла."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_csv(path: Path, rows: List[Tuple[str, int]]) -> None:
    """Записывает частоты слов в CSV."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(rows)