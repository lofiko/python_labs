import argparse
import sys
import os
from pathlib import Path

# Добавляем путь к src, чтобы импортировать lib/text.py
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from lib.text import normalize, tokenize, count_freq, top_n


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description="CLI-утилита для работы с текстом (cat, stats)"
    )
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser(
        "cat",
        help="Вывести содержимое файла",
        description="Вывести содержимое текстового файла построчно.",
    )
    cat_parser.add_argument(
        "--input",
        required=True,
        help="Путь к файлу",
    )
    cat_parser.add_argument(
        "-n",
        dest="number",
        action="store_true",
        help="Нумеровать строки",
    )

    # подкоманда stats
    stats_parser = subparsers.add_parser(
        "stats",
        help="Показать топ-N слов",
        description="Показать топ-N самых частых слов в файле.",
    )
    stats_parser.add_argument(
        "--input",
        required=True,
        help="Путь к файлу",
    )
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Сколько слов вывести (по умолчанию 5)",
    )

    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "cat":
            file_path = Path(args.input)

            if not file_path.is_file():
                print(f"Ошибка: файл '{file_path}' не найден.", file=sys.stderr)
                raise FileNotFoundError(file_path)

            with file_path.open("r", encoding="utf-8") as f:
                for num, line in enumerate(f, start=1):
                    line = line.rstrip("\n")
                    if args.number:
                        print(f"{num:>2}. {line}")
                    else:
                        print(line)

        elif args.command == "stats":
            file_path = Path(args.input)

            if not file_path.is_file():
                print(f"Ошибка: файл '{file_path}' не найден.", file=sys.stderr)
                raise FileNotFoundError(file_path)

            text = file_path.read_text(encoding="utf-8")

            if not text.strip():
                print("Файл пуст — статистику не посчитать.", file=sys.stderr)
                return

            normalized = normalize(text, casefold=True, yo2e=True)
            tokens = tokenize(normalized)
            freq = count_freq(tokens)
            top_words = top_n(freq, args.top)

            print(f"Топ-{args.top} слов в файле '{args.input}':")

            max_len = max(len(word) for word, _ in top_words)
            for word, count in top_words:
                print(f"{word.ljust(max_len)}   {count}")

        else:
            parser.print_help()

    except FileNotFoundError:
        sys.exit(1)


if __name__ == "__main__":
    main()
