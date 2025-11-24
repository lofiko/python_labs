import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("\t\n   ", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


def test_normalize_no_casefold_no_yo2e():
    """Параметры casefold / yo2e должны реально влиять на результат."""
    text = "ЁЖик Мир"

    assert normalize(text, casefold=False, yo2e=False) == "ЁЖик Мир"

    assert normalize(text, casefold=False, yo2e=True) == "еЖик Мир"

    assert normalize(text, casefold=True, yo2e=False) == "ёжик мир"


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("один, два, три!", ["один", "два", "три"]),
        (
            "привет мир, привет-привет!",
            ["привет", "мир", "привет-привет"],
        ),
        ("", []),
        ("   много   пробелов   ", ["много", "пробелов"]),
        ("слово слово слово", ["слово", "слово", "слово"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
    ],
)
def test_tokenize(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),
        (["x"], {"x": 1}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq_dict, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, [("a", 3), ("b", 2), ("c", 1)]),
        (
            {"яблоко": 2, "апельсин": 2, "банан": 2},
            [("апельсин", 2), ("банан", 2), ("яблоко", 2)],
        ),
        ({}, []),
        (
            {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1, "f": 1},
            [("a", 5), ("b", 4), ("c", 3), ("d", 2), ("e", 1)],
        ),
    ],
)
def test_top_n_default(freq_dict, expected):
    assert top_n(freq_dict) == expected


def test_top_n_custom_n_and_bounds():
    freq = {"a": 3, "b": 2, "c": 1}

    assert top_n(freq, n=2) == [("a", 3), ("b", 2)]
    assert top_n(freq, n=0) == []
    assert top_n(freq, n=10) == [("a", 3), ("b", 2), ("c", 1)]
