import datetime

# Рядок 4
with open('data/names.txt', 'r', encoding='utf-8') as f:
# Рядок 5: ПЕРЕВІРТЕ: Тут мають бути 4 пробіли
    names = [line.strip() for line in f]
    
current_time = datetime.datetime.now().strftime("%H:%M:%S")

for name in names:
# Рядок 9: ПЕРЕВІРТЕ: Тут мають бути 4 пробіли
    print(f"Привіт, {name}! Поточний час: {current_time}")    