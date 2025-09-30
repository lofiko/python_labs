fio = input("ФИО: ")

initials = "".join([word[0] for word in fio.split()])
fio_probeli = fio.replace(" ", "")
length = len(fio_probeli)

print(f"Инициалы: {initials}")
print(f"Длина (символов): {length+2}")