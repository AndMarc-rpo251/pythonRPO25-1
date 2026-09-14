"""ОСНОВНОЙ ФАЙЛ ПРИЛОЖЕНИЯ Task Manager
   version 0.0.4
--- description ---
приложение может сохранять, редактировать, удалять задачи
"""

collection = ['йоу'] #list
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
            waite = input("Нажмите ENTER, чтобы продолжить")

        case '2':
            write = input('Введите заметку: ')
            if not write.strip():
                print('Заметка не может быть пустой')
                continue
            collection.append(write)
            show_collection(collection)
            waite = input("Нажмите ENTER, чтобы продолжить")

        case '3':
            print("выберите заметку")
            show_collection(collection)
            select_delet = int(input())
            if int(select_delet) <= len(collection) and select_delet > 0:
                collection.pop(select_delet -1)
                print('заметка удалена')
            else:
                print('Такой заметки нет')
            waite = input("Нажмите ENTER, чтобы продолжить")

        case '4':
            show_collection(collection)
            select_edit = input('Введите номер задачи для редактирования')

            if not select_edit.isdigit():
                continue
            select_edit = int(select_edit)
            if select_edit > 0 and select_edit <= len(collection):
                edit_name = input('Введите новое название')
                collection[select_edit - 1] = edit_name
                show_collection(collection)
                print('Успешно изменено. Нажмите ENTER, чтобы продолжить')
            else:
                print('такой задачи нет')

        case '0':
            is_running = False

        case _:
            print('Такого пункта нет')
            show_collection(collection)
            waite = input("Нажмите ENTER, чтобы продолжить")


