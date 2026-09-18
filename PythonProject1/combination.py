import math
import tkinter
import tkinter.ttk as ttk


def calculate():
    try:
        n = int(entry_n.get())
        k = int(entry_k.get())

        if n < 0 or k < 0:
            result_label.config(text="Ошибка: числа не могут быть отрицательными")
            return

        if k > n:
            result_no_repeat = "Размещения: невозможно (k > n)"
            combination_no_repeat = "Сочетания: невозможно (k > n)"
        else:
            # БЕЗ повторений
            P = math.factorial(n)
            A = math.factorial(n) // math.factorial(n - k)
            C = math.factorial(n) // (
                math.factorial(k) * math.factorial(n - k)
            )

            result_no_repeat = (
                f"Перестановки: {P}\n"
                f"Размещения: {A}\n"
                f"Сочетания: {C}"
            )

        # С ПОВТОРЕНИЯМИ
        # Размещения с повторениями
        A_repeat = n ** k

        # Сочетания с повторениями
        C_repeat = math.factorial(n + k - 1) // (
            math.factorial(k) * math.factorial(n - 1)
        )

        # Вывод
        result_label.config(
            text=
            "БЕЗ ПОВТОРЕНИЙ\n"
            + result_no_repeat
            + "\n\n"
            + "С ПОВТОРЕНИЯМИ\n"
            + f"Размещения: {A_repeat}\n"
            + f"Сочетания: {C_repeat}"
        )

    except ValueError:
        result_label.config(text="Ошибка: введите целые числа")


# Создаём окно
window = tkinter.Tk()
window.title("Комбинаторика")
window.geometry("450x450")


# Заголовок
title = ttk.Label(
    window,
    text="Комбинаторика",
    font=("Arial", 18)
)
title.pack(pady=15)


# n
label_n = ttk.Label(window, text="Введите n:")
label_n.pack()

entry_n = ttk.Entry(window)
entry_n.pack(pady=5)


# k
label_k = ttk.Label(window, text="Введите k:")
label_k.pack()

entry_k = ttk.Entry(window)
entry_k.pack(pady=5)


# Кнопка
button = ttk.Button(
    window,
    text="Рассчитать",
    command=calculate
)
button.pack(pady=15)


# Результат
result_label = ttk.Label(
    window,
    text="",
    font=("Arial", 11),
    justify="left"
)
result_label.pack(pady=10)


# Запуск
window.mainloop()
