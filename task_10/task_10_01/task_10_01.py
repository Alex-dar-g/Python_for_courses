"""
Задание 10.01
Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""


# a)
def work_with_file_a(some_file: str) -> str:
    """
    Write from file first line
    """
    if not isinstance(some_file, str):
        print("Введите имя файла")
    with open(some_file, 'r') as my_file:
        lines = my_file.readlines()
    return lines[0]


print(work_with_file_a('test.txt'))


# b)
def work_with_file_b(some_file: str) -> str:
    """
    Write from file fifth line
    """
    if not isinstance(some_file, str):
        print("Введите имя файла")
    with open(some_file, 'r') as my_file:
        lines = my_file.readlines()
    return lines[4]


print(work_with_file_b('test.txt'))


# c)
def work_with_file_c(some_file: str):
    """
    Write from the file from the first line to the fifth
    """
    if not isinstance(some_file, str):
        print("Введите имя файла")
    with open(some_file, 'r') as my_file:
        lines = my_file.readlines()
    count_line = 0
    while count_line < 6:
        print(lines[count_line])
        count_line += 1


print(work_with_file_c('test.txt'))


# d)
def work_with_file_d(some_file: str):
    """
    Write from the file from the "first_num" line to the "second_num"
    """
    if not isinstance(some_file, str):
        print("Введите имя файла")
    with open(some_file, 'r') as my_file:
        lines = my_file.readlines()
        first_num = input("Введите номер строки с которой вы хотите прочитать файл: ")
        second_num = input("Введите номер строки до которой вы хотите прочитать файл: ")
        # проверка вводимых данных на int
        if not isinstance(first_num, int) and isinstance(second_num, int):
            print("Введите только число")

        integer_first_num, integer_second_num = int(first_num) - 1, int(second_num)
        list_rows = lines[integer_first_num:integer_second_num]
        for line in list_rows:
            print(line)


print(work_with_file_d('test.txt'))


# e)
def work_with_file_e(some_file: str):
    """
    Write from the file all lines
    """
    if not isinstance(some_file, str):
        print("Введите имя файла")
    with open(some_file, 'r') as my_file:
        lines = my_file.readlines()
        for line in lines:
            print(line)


print(work_with_file_e('test.txt'))
