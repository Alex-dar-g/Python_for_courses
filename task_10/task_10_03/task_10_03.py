"""
Задание 10.03
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""


def input_string(some_file: str):
    """
    Write 3 lines in end file, which user input with keyboard
    """
    if not isinstance(some_file, str):
        print('Введите имя файла')
    with open(some_file, 'a', encoding="UTF-8") as my_file:
        for _ in range(3):
            my_file.write("\n" + input("Введите строку, которую вы хотите занести в файл: "))


print(input_string('some_text.txt'))
