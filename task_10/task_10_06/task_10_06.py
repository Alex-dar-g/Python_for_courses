"""
Задание 10.06
Имеются два текстовых файла с одинаковым числом
строк. Выяснить, совпадают ли их строки. Если нет, то
получить номер первой строки, в которой эти файлы
отличаются друг от друга.
"""


def compare_two_files(first_file_txt: str, second_file_txt: str):
    """
        Function for check 2 files an identical lines and print number first identical line
    """
    with open(first_file_txt, 'r') as first_file:
        lines_first_file = first_file.readlines()
    with open(second_file_txt, 'r') as second_file:
        lines_second_file = second_file.readlines()
    # поскольку длина двух файлов совпадает, поэтому возьму длину первого файла
    count_lines = 0
    length_lines = len(lines_first_file)
    while count_lines <= length_lines:
        if not lines_first_file[count_lines] == lines_second_file[count_lines]:
            return f'Номер первой строки, по которой файлы не совпадают: {count_lines + 1}'
        count_lines += 1


print(compare_two_files('first_file.txt', 'second_file.txt'))
