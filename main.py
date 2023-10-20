import random

lines = []
students = {}

def open_table():
    with open('names.txt', 'r') as fr, open('db.txt', 'w') as fw:
        fw.write(''.join(fr.readlines()))
    with open('db.txt', 'r') as file:
        for row in file:
            row1 = row.strip().split()
            lines.append(row1)
    for student in lines:
        students[student[0]] = [student[1], student[2], student[3]]

def print_data_base():
    for key in students:
        print(*students[key])
    with open('db.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))

def unique_student(surname, name):
    for i in students:
        flag = True
        if surname == students[i][0] and name == students[i][1]:
            flag = False
            break
        else:
            flag = True
    return flag


def del_student():
    i = int(input('Введите ID студента '))
    id = str(i)
    if id in students:
        print(f'Студент {students[id][0]} {students[id][1]} удалён из БД')
        del students[id]
    else:
        print('Студента с таким ID не существует')
    with open('db.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))

def add_student_by_id():
    i = int(input('Введите номер '))
    surname, name, = '', '', ''
    id = str(i)
    if id in students:
        print('Студент с таким ID уже существует')
    else:
        s, n, p = [i for i in input('Введите фамилию ').split()], [i for i in input('Введите имя ').split()]
        surname, name, patronymic = ''.join(s), ''.join(n), ''.join(p)
        if unique_student(surname, name):
            students.update(id = [surname, name, '0'])
            students[id] = students.pop('id')
            students[id][3] = str(random.randint(1, 100))
            with open('db.txt', 'w') as file:
                for key, value in students.items():
                    file.write('{} {}\n'.format(key, ' '.join(value)))
        else:
            print('Студент с таким ФИО уже существует')


def add_student_by_fio():
    s, n = [i for i in input('Введите фамилию ').split()], \
              [i for i in input('Введите имя ').split()]
    surname, name = ''.join(s), ''.join(n)
    id = random.randint(1, 1000)
    if id in students:
        while id in students:
            id = random.randint(1, 1000)
    id = str(id)
    if unique_student(surname, name):
        students.update(id = [surname, name, '0'])
        students[id] = students.pop('id')
        students[id][3] = str(random.randint(1, 100))
        with open('db.txt', 'w') as file:
            for key, value in students.items():
                file.write('{} {}\n'.format(key, ' '.join(value)))
    else:
        print('Студент с таким именем уже существует')


def get_student():
    id = input('Введите ID студента ')
    if id in students:
        print(*students[id])
    else:
        print('Студент с таким ID не существует')

def show_id():
    for key in students:
        print(key)

def edit_student():
    id = input('Введите ID студента ')
    surname, name = '', ''
    if id in students:
        print(*students[id])
        choice = input('Что вы хотите изменить? ф - фамилия, и - имя, в - всё ')
        if choice == 'ф':
            s = [i for i in input('Введите фамилию ').split()]
            surname = ''.join(s)
            students[id][0] = surname
            print('Фамилия успешно изменена')
        elif choice == 'и':
            n = [i for i in input('Введите имя ').split()]
            name = ''.join(n)
            students[id][1] = name
            print('Имя успешно изменено')
        elif choice == 'в':
            s, n, p = [i for i in input('Введите фамилию ').split()], [i for i in input('Введите имя ').split()]
            surname, name = ''.join(s), ''.join(n)
            if unique_student(surname, name):
                students[id][0], students[id][1] = surname, name
                print('ФИО студента успешно изменены')
            else:
                print('Студент с таким именем уже существует')
        else:
            print('Введите другую букву')
    else:
        print('Студента с таким ID не существует')
    with open('db.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))

def give_variant():
    lst = [str(i) for i in range(1, 100)]
    for id in students:
        if id != 'ID':
            students[id][3] = random.choice(lst)
    print('Варианты успешно выданы')
    with open('db.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))

def testing_table():
    with open('testing table.txt', 'w') as file:
        for key in students:
            file.write(f'{key} {students[key][3]}\n')
    print('Таблица отправлена учителю')

def save_table():
    with open('saved.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))
    print('Таблица успешно сохранена')

def backup():
    with open('saved.txt', 'r') as fr, open('db.txt', 'w') as fw:
        fw.write(''.join(fr.readlines()))
    with open('db.txt', 'r') as file:
        for row in file:
            row1 = row.strip().split()
            lines.append(row1)
    for student in lines:
        students[student[0]] = [student[1], student[2], student[3]]

def main():
    print('Введите команду.\nopen - открыть таблицу, print - печать БД, addByID - добавить студента по ID,\n'
          'addByFIO - добавить студента по ФИО, del - удалить данные студента, get - получить данные студента,\n'
          'show - показать все доступные ID, edit - редактировать данные студента, var - раздать вариант,\n'
          'send - отправить учителю, save - сохранить таблицу,\n'
          'backup - открыть последнее сохранение, end - завершить работу.')
    while True:
        choice = input()
        if choice == 'open':
            open_table()
        elif choice == 'print':
            print_data_base()
        elif choice == 'addByID'.lower():
            add_student_by_id()
        elif choice == 'addByFIO'.lower():
            add_student_by_fio()
        elif choice == 'del':
            del_student()
        elif choice == 'get':
            get_student()
        elif choice == 'show':
            show_id()
        elif choice == 'edit':
            edit_student()
        elif choice == 'var':
            give_variant()
        elif choice == 'send':
            testing_table()
        elif choice == 'save':
            save_table()
        elif choice == 'backup':
            backup()
        elif choice == 'end':
            break
        else:
            print('Такой команды не существует')

if __name__ == '__main__':
    main()
  
