"""ОСНОВНОЙ ФАЙЛ ПРИЛОЖЕНИЯ Task Manager
   version 0.0.1
  -[x] создать основной цикл задач
  -[x] сделать функцию - показать заметки
  -[x] сделать функцию - добавить заметки"""
from random import choice

collection = [] #list
is_start = True #flag

while (is_start):
    print('1 - показать задачи | 2 - добавить заметки')
    choice_user = input('Введите ваш выбор (1 или 2)')
    match choice_user:
        case '1':
            print(collection)
        case '2':
            collection.append('task')
            print(collection)
        case _:
            print('Такого пункта нет')
