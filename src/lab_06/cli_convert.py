import argparse
from pathlib import Path
import sys
import os

# путь к src, чтобы импортировать функции из lab05
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lab_05.json_csv import json_to_csv, csv_to_json
from lab_05.csv_to_xlsx import csv_to_xlsx


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Конвертеры данных (JSON <-> CSV <-> XLSX)"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="Команды",
        description="Доступные подкоманды: json2csv, csv2json, csv2xlsx",
    )

    # json2csv
    p1 = subparsers.add_parser("json2csv", help="- Конвертация JSON → CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON-файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV-файл")

    # csv2json
    p2 = subparsers.add_parser("csv2json", help="- Конвертация CSV → JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON-файл")

    # csv2xlsx
    p3 = subparsers.add_parser("csv2xlsx", help="- Конвертация CSV → XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX-файл")

    return parser


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    # 1) Нет аргументов → короткое меню
    if not argv:
        print("CLI-конвертер данных (json2csv, csv2json, csv2xlsx)\n")
        print("Команды:")
        print("  json2csv  - Конвертация JSON → CSV")
        print("  csv2json  - Конвертация CSV → JSON")
        print("  csv2xlsx  - Конвертация CSV → XLSX\n")
        print("Использование:")
        print(
            "  python3 src/lab_06/cli_convert.py (json2csv/csv2json/csv2xlsx) --in data/samples/файл --out data/out/файл\n"
        )
        return

    # 2) Общий help
    if argv[0] in ("-h", "--help"):
        print("Справка по конвертерам данных\n")
        print("Команды:")
        print("  json2csv  - Конвертация JSON → CSV")
        print("  csv2json  - Конвертация CSV → JSON")
        print("  csv2xlsx  - Конвертация CSV → XLSX\n")
        print("Дополнительно:")
        print("  python3 src/lab_06/cli_convert.py json2csv --help")
        print("  python3 src/lab_06/cli_convert.py csv2json --help")
        print("  python3 src/lab_06/cli_convert.py csv2xlsx --help\n")
        return

    # 3) help для json2csv
    if argv[0] == "json2csv" and len(argv) > 1 and argv[1] in ("-h", "--help"):
        print("Справка по команде: json2csv\n")
        print("Назначение:")
        print("  Конвертация JSON → CSV\n")
        print("Параметры:")
        print("  --in или --input ПУТЬ    Входной JSON-файл")
        print("  --out или --output ПУТЬ   Выходной CSV-файл\n")
        print("Пример:")
        print(
            "  python3 src/lab_06/cli_convert.py json2csv --in data/samples/файл.json --out data/out/файл.csv\n"
        )
        return

    # 4) help для csv2json
    if argv[0] == "csv2json" and len(argv) > 1 and argv[1] in ("-h", "--help"):
        print("Справка по команде: csv2json\n")
        print("Назначение:")
        print("  Конвертация CSV → JSON\n")
        print("Параметры:")
        print("  --in или --input ПУТЬ    Входной CSV-файл")
        print("  --out или --output ПУТЬ   Выходной JSON-файл\n")
        print("Пример:")
        print(
            "  python3 src/lab_06/cli_convert.py csv2json --in data/samples/файл.csv --out data/out/файл.json\n"
        )
        return

    # 5) help для csv2xlsx
    if argv[0] == "csv2xlsx" and len(argv) > 1 and argv[1] in ("-h", "--help"):
        print("Справка по команде: csv2xlsx\n")
        print("Назначение:")
        print("  Конвертация CSV → XLSX (Excel)\n")
        print("Параметры:")
        print("  --in ПУТЬ    Входной CSV-файл")
        print("  --out ПУТЬ   Выходной XLSX-файл\n")
        print("Пример:")
        print(
            "  python3 src/lab_06/cli_convert.py csv2xlsx --in data/samples/файл.csv --out data/out/файл.xlsx\n"
        )
        return

    # 6) Основная логика
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
            print(f"Создан файл: {args.output}")

        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
            print(f"Создан файл: {args.output}")

        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print(f"Создан файл: {args.output}")

        else:
            print("Неизвестная команда. Используй --help.")
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден ({e})")
        sys.exit(1)


if __name__ == "__main__":
    main()
