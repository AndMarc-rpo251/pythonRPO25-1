"""ОСНОВНОЙ ФАЙЛ ПРИЛОЖЕНИЯ Task Manager
   version 0.0.1
  -[x] создать основной цикл задач
  -[x] сделать функцию - показать заметки
  -[x] сделать функцию - добавить заметки"""

collection = [] #list
is_start = True #flag

while (is_start):
    print('1 - показать задачи | 2 - добавить заметки | 3 - удалить заметку')
    choice_user = input('Введите ваш выбор (1, 2, 3)')
    match choice_user:
        case '1':
            print(collection)
        case '2':
            collection.append(input())
            print(collection)
        case '3':
            print("выберите заметку", collection)
            a = input()
            if a in collection:
                collection.remove(a)
                print('заметка удалена')
            else:
                print('Такой заметки нет')
            print(collection)
        
        case _:
            print('Такого пункта нет')
