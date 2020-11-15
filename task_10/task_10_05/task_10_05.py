"""
Задание 10.05
Имеется текстовый файл. Все четные строки этого файла
записать во второй файл, а нечетные — в третий файл.
Порядок следования строк сохраняется.
"""


def output_strings(name_file: str):
    """
        Function write even lines and uneven lines in other files
    """
    if not isinstance(name_file, str):
        print('Введите имя файла')

    with open(name_file, 'r') as const_file:
        lines = const_file.readlines()
        # проверка, является ли файл пустым
        for line in lines:
            if not line:
                break
        try:
            length_lines = len(lines)
            with open('first_file.txt', 'w') as first_file:
                # заводим счётчик для печати чётных строк
                count_for_even_lines = 0
                while count_for_even_lines <= length_lines:
                    first_file.writelines(lines[count_for_even_lines])
                    count_for_even_lines += 2

            with open('second_file.txt', 'w') as second_file:
                count_for_uneven_lines = 1
                # заводим счётчик для печати нечётных строк
                while count_for_uneven_lines <= length_lines:
                    second_file.writelines(lines[count_for_uneven_lines])
                    count_for_uneven_lines += 2
        except IndexError:
            pass


print(output_strings('const_file.txt'))
