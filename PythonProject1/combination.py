import math
import tkinter
import tkinter.ttk as ttk


def calculate():
    n = int(entry_n.get())
    k = int(entry_k.get())

    if k > n:
        result_label.config(text="Ошибка: k не может быть больше n")
        return

    # Перестановки
    P = math.factorial(n)

    # Размещения
    A = math.factorial(n) // math.factorial(n - k)

    # Сочетания
    C = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    result_label.config(
        text=f"Перестановки: {P}\n"
             f"Размещения: {A}\n"
             f"Сочетания: {C}"
    )


# Создаём окно
window = tkinter.Tk()
window.title("Комбинаторика")
window.geometry("400x300")


# Заголовок
title = ttk.Label(window, text="Комбинаторика")
title.pack(pady=10)


# Поле для n
label_n = ttk.Label(window, text="Введите n:")
label_n.pack()

entry_n = ttk.Entry(window)
entry_n.pack(pady=5)


# Поле для k
label_k = ttk.Label(window, text="Введите k:")
label_k.pack()

entry_k = ttk.Entry(window)
entry_k.pack(pady=5)


# Кнопка
button = ttk.Button(window, text="Рассчитать", command=calculate)
button.pack(pady=10)


# Результат
result_label = ttk.Label(window, text="")
result_label.pack(pady=10)


# Запуск окна
window.mainloop()
