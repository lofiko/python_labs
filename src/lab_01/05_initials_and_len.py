fio = input("ФИО: ")

initials = "".join([word[0] for word in fio.split()])
length = len(fio)

print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")