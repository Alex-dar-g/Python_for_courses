"""
Задание 10.02
Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры.
"""


def input_string(some_file: str):
    """
    Func for write lines in file, which user input with keyboard
    """
    if not isinstance(some_file, str):
        print('Введите имя файла')
    with open(some_file, 'w') as my_file:
        for _ in range(6):
            my_file.write(input("Введите строку, которую вы хотите занести в файл: ") + "\n")


print(input_string('test_for_input.txt'))
