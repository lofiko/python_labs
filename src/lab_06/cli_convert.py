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
        metavar="команда",
    )

    # json2csv
    p1 = subparsers.add_parser(
        "json2csv",
        help="Конвертация JSON → CSV",
        description="Конвертация данных из JSON-файла в CSV-файл.",
    )
    p1.add_argument(
        "--in",
        "--input",
        dest="input",
        required=True,
        help="Входной JSON-файл",
        metavar="ПУТЬ",
    )
    p1.add_argument(
        "--out",
        "--output",
        dest="output",
        required=True,
        help="Выходной CSV-файл",
        metavar="ПУТЬ",
    )
    p1.set_defaults(func=lambda args: json_to_csv(args.input, args.output))

    # csv2json
    p2 = subparsers.add_parser(
        "csv2json",
        help="Конвертация CSV → JSON",
        description="Конвертация данных из CSV-файла в JSON-файл.",
    )
    p2.add_argument(
        "--in",
        "--input",
        dest="input",
        required=True,
        help="Входной CSV-файл",
        metavar="ПУТЬ",
    )
    p2.add_argument(
        "--out",
        "--output",
        dest="output",
        required=True,
        help="Выходной JSON-файл",
        metavar="ПУТЬ",
    )
    p2.set_defaults(func=lambda args: csv_to_json(args.input, args.output))

    # csv2xlsx
    p3 = subparsers.add_parser(
        "csv2xlsx",
        help="Конвертация CSV → XLSX",
        description="Конвертация данных из CSV-файла в XLSX (Excel).",
    )
    p3.add_argument(
        "--in",
        "--input",
        dest="input",
        required=True,
        help="Входной CSV-файл",
        metavar="ПУТЬ",
    )
    p3.add_argument(
        "--out",
        "--output",
        dest="output",
        required=True,
        help="Выходной XLSX-файл",
        metavar="ПУТЬ",
    )
    p3.set_defaults(func=lambda args: csv_to_xlsx(args.input, args.output))

    return parser


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = build_parser()
    args = parser.parse_args(argv)

    # Если подкоманда не указана — показать общий help
    if args.command is None:
        parser.print_help()
        sys.exit(1)

    try:
        # вызываем функцию, привязанную к подкоманде
        args.func(args)
        print(f"Создан файл: {args.output}")
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден ({e})", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
