import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import csv
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path: Path, xlsx_path: Path) -> None:
    """
    Конвертирует CSV-файл в XLSX (Excel).
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            ws.append(row)

    wb.save(xlsx_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python3 csv_to_xlsx.py <режим> <input_file>")
        print("Режимы: csv2xlsx")
        sys.exit(1)

    mode = sys.argv[1].lower()
    input_file = sys.argv[2]

    base = Path(__file__).resolve().parent.parent.parent
    out_dir = base / "data" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)

    input_path = Path(input_file)

    if mode == "csv2xlsx":
        output_file = out_dir / f"{input_path.stem}.xlsx"
        csv_to_xlsx(input_file, output_file)
        print(f"Создан: {output_file}")

    else:
        print("Неизвестный режим. Используйте: csv2xlsx")
