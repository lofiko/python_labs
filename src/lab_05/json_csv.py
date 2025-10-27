import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pathlib import Path
import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not json_path.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Некорректный JSON-файл")

    if not isinstance(data, list) or not data:
        raise ValueError()

    # Сбор всех возможных ключей (чтобы заполнить пропуски пустыми строками)
    all_keys = set()
    for item in data:
        if not isinstance(item, dict):
            raise ValueError()
        all_keys.update(item.keys())

    # Порядок колонок — как в первом объекте, затем остальные по алфавиту
    first_keys = list(data[0].keys())
    remaining_keys = sorted(all_keys - set(first_keys))
    headers = first_keys + remaining_keys

    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for item in data:
            row = {key: item.get(key, "") for key in headers}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV не содержит заголовок")

        data = list(reader)
        if not data:
            raise ValueError("CSV пуст")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python3 src/lab_05/json_csv.py <режим> <input_file>")
        print("Режимы: json2csv, csv2json")
        sys.exit(1)

    mode = sys.argv[1].lower()
    input_file = sys.argv[2]
    
    # Определяем базовую директорию относительно расположения скрипта
    base = Path(__file__).resolve().parent.parent.parent
    out_dir = base / "data" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)

    input_path = Path(input_file)
    
    if mode == "json2csv":
        output_file = out_dir / f"{input_path.stem}.csv"
        json_to_csv(input_file, output_file)
        print(f"Создан: {output_file}")
        
    elif mode == "csv2json":
        output_file = out_dir / f"{input_path.stem}.json"
        csv_to_json(input_file, output_file)
        print(f"Создан: {output_file}")
        
    else:
        print("Неизвестный режим. Используйте: json2csv или csv2json")
