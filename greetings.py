import datetime

name = input("Введіть ваше ім'я: ")

current_time = datetime.datetime.now().strftime("%H:%M:%S")

print(f"Привіт, {name}! Поточний час: {current_time}")