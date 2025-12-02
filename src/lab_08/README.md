# Лабораторная работа 8  
## ООП, dataclass и сериализация JSON (Python)

---

## 📌 Цель работы

Изучить:
- создание классов и объектную модель Python,
- использование `@dataclass`,
- методы экземпляра (`age`, `__str__`, сериализация),
- механизм `__post_init__` и валидацию полей,
- сериализацию/десериализацию JSON,
- структуру модулей и работу с пакетами.

---

## 📁 Структура репозитория

```text
python_labs/
├─ src/
│  └─ lab_08/
│     └─ README.md   ← этот отчёт
│     └─ main.py
│     └─ models.py
│     └─ serialize.py
│
└─ README.md/
```

## 📄 Мой файл models.py

```python
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # Проверка формата даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid birthdate format: {self.birthdate}. Expected YYYY-MM-DD")

        # Проверка диапазона GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA must be between 0 and 5")

    def age(self) -> int:
        # Кол-во полних лет
        bdate = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - bdate.year
        if (today.month, today.day) < (bdate.month, bdate.day):
            years -= 1
        return years

    def to_dict(self) -> dict:
        # Сериализация в словарь
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        # Создание объекта из словаря
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"]),
        )

    def __str__(self):
        return f"{self.fio} ({self.group}), GPA={self.gpa}, age={self.age()} y/o"
```

## 📄 Мой файл serialize.py

```python
import json
from .models import Student


def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Student.from_dict(item) for item in raw]
```

## 📄 Мой файл data/lab_08/students_input.json

```json
[
  {
    "fio": "Карташов Филипп Дмитриевич",
    "birthdate": "2007-08-10",
    "group": "БИВТ-25-8",
    "gpa": 4.6
  },
  {
    "fio": "Иванов Иван Иванович",
    "birthdate": "2006-04-20",
    "group": "ПМ-22-4",
    "gpa": 3.9
  }
]
```

## Вывод в терминале

![terminal](../../images/lab_08/terminal.png)

### После выполнения программы, был создан файл students_output.json

![output](../../images/lab_08/output.png)