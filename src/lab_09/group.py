import os
import sys
import csv
from pathlib import Path
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lab_08')))
from models import Student


HEADER = ["fio", "birthdate", "group", "gpa"]


class Group:
    """
    CSV-based student storage with CRUD operations and analytics.
    """

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Create CSV file with header if it does not exist."""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(HEADER)

    def _read_all(self) -> List[Student]:
        """Load all rows from CSV → list[Student]."""
        students = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames != HEADER:
                raise ValueError(
                    f"Invalid CSV header. Expected {HEADER}, got {reader.fieldnames}"
                )

            for row in reader:
                try:
                    students.append(
                        Student(
                            fio=row["fio"],
                            birthdate=row["birthdate"],
                            group=row["group"],
                            gpa=float(row["gpa"]),
                        )
                    )
                except Exception as e:
                    raise ValueError(f"Invalid row in CSV: {row}") from e

        return students

    def _write_all(self, students: List[Student]) -> None:
        """Rewrite CSV file with the given student list."""
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADER)
            writer.writeheader()
            for st in students:
                writer.writerow(
                    {
                        "fio": st.fio,
                        "birthdate": st.birthdate,
                        "group": st.group,
                        "gpa": st.gpa,
                    }
                )

    # CRUD OPERATIONS
    def list(self) -> List[Student]:
        """Return all students."""
        return self._read_all()

    def add(self, student: Student) -> None:
        """Add a new student (no duplicates by FIO)."""
        students = self._read_all()

        if any(st.fio == student.fio for st in students):
            raise ValueError(f"Student already exists: {student.fio}")

        students.append(student)
        self._write_all(students)

    def find(self, substr: str) -> List[Student]:
        """Find students whose FIO contains the given substring."""
        substr = substr.lower()
        return [st for st in self._read_all() if substr in st.fio.lower()]

    def remove(self, fio: str) -> None:
        """Delete the student with the exact FIO."""
        students = self._read_all()
        new = [st for st in students if st.fio != fio]

        if len(new) == len(students):
            raise ValueError(f"No student with fio: {fio}")

        self._write_all(new)

    def update(self, fio: str, **fields) -> None:
        """
        Update fields of an existing student.
        Example:
            group.update("Ivanov Ivan", gpa=4.9, group="SE-01")
        """
        students = self._read_all()
        updated = False

        for st in students:
            if st.fio == fio:
                for key, value in fields.items():
                    if not hasattr(st, key):
                        raise ValueError(f"Unknown field: {key}")
                    setattr(st, key, value)
                updated = True
                break

        if not updated:
            raise ValueError(f"No student with fio: {fio}")

        self._write_all(students)

    # ANALYTICS (★ optional)
    def stats(self) -> dict:
        """Return analytics: count, min/max/avg GPA, group distribution, top 5."""
        students = self._read_all()

        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": [],
            }

        gpas = [st.gpa for st in students]

        # Group → count
        group_counts = {}
        for st in students:
            group_counts[st.group] = group_counts.get(st.group, 0) + 1

        # Top 5 by GPA
        top_5 = sorted(students, key=lambda s: s.gpa, reverse=True)[:5]

        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": group_counts,
            "top_5_students": [{"fio": st.fio, "gpa": st.gpa} for st in top_5],
        }