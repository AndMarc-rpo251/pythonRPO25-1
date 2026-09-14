"""ОСНОВНОЙ ФАЙЛ ПРИЛОЖЕНИЯ Task Manager
   version 0.0.4
--- description ---
приложение может сохранять, редактировать, удалять задачи
"""

collection = [] #list
is_running = True #flag


def show_collection(task_collection):
    for i, j in enumerate(task_collection):
        print(i + 1, j)
    print("`~"*30)

while (is_running):
    print('1 - показать задачи | 2 - добавить заметки | 3 - удалить заметку | 4 - редактировать заметку | 0 - выход')
    choice_user = input('Введите ваш выбор (1, 2, 3, 4, 0)')
    match str(choice_user):
        case '1':
            show_collection(collection)
        case '2':
            collection.append(input())
            show_collection(collection)
        case '3':
            print("выберите заметку", collection)
            a = input()
            if a in collection:
                collection.remove(a)
                print('заметка удалена')
            else:
                print('Такой заметки нет')
            show_collection()
        case '4':
            for i, j in enumerate(collection):
                print(i + 1, j)
            select_task = int(input('Введите номер задачи для редактирования'))
            edit_task = input('Введите новое название')
            collection[select_task - 1] = edit_task
            show_collection(collection)
        case '0':
            is_running = False
        case _:
            print('Такого пункта нет')
            show_collection(collection)
