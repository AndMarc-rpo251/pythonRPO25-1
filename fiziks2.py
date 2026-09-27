import random

def is_safe_pin(pin: str) -> bool:

    # Все цифры одинаковые
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return False

    # Строго по порядку (каждая следующая цифра на 1 больше предыдущей)
    if (int(pin[1]) - int(pin[0]) == 1 and
        int(pin[2]) - int(pin[1]) == 1 and
        int(pin[3]) - int(pin[2]) == 1):
        return False

    return True

def generate_safe_pin() -> str:
    while True:
        # Генерируем случайную строку из 4 цифр
        pin = (
            str(random.randint(0, 9)) +
            str(random.randint(0, 9)) +
            str(random.randint(0, 9)) +
            str(random.randint(0, 9))
        )
        if is_safe_pin(pin):
            return pin


# Примеры использования
if __name__ == "__main__":
    print("Комбинаторный расчёт:")
    print(f"Всего возможных ПИН-кодов: 10000")
    print(f"Отсеивается опасных: 17")
    print()

    print("Примеры сгенерированных безопасных ПИН-кодов:")
    for i in range(10):
        print(generate_safe_pin())
