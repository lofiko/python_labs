import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.lab_08.serialize import students_from_json, students_to_json


def main():
    students = students_from_json("data/lab_08/students_input.json")
    for s in students:
        print(s)

    students_to_json(students, "data/lab_08/students_output.json")


if __name__ == "__main__":
    main()
