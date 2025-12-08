from group import Group
from models import Student

g = Group("/Users/kofil/vscode_pr/python_labs/data/lab_09/students.csv")

print("=== ИЗНАЧАЛЬНЫЙ СПИСОК ===:")
print(*g.list(), sep="\n")

print("\n=== add() ===")
s = Student("Тестовый Студент", "2005-05-05", "TEST-01", 4.5)
g.add(s)
print(*g.list(), sep="\n")

print("\n=== find('Тест') ===")
print(g.find("Тест"))

print("\n=== update() ===")
g.update("Тестовый Студент", gpa="4.9")
print(g.find("Тест"))
print(*g.list(), sep="\n")

print("\n=== remove() ===")
g.remove("Тестовый Студент")
print(*g.list(), sep="\n")

print("\n=== stats() ===")
print(g.stats())