"""
Задание 10.04
Имеется текстовый файл. Переписать в другой файл все
его строки с заменой в них символа 0 на символ 1 и
наоборот.
"""


def reverse_numbers(name_file: str):
    """
    Swap in file 0=1 and 1=0
    """
    if not isinstance(name_file, str):
        print('Введите имя файла')
    with open(name_file, 'r') as const_file:
        with open('output_file.txt', 'w') as output_file:
            for line in const_file.readlines():
                if not line:
                    break
                # производим замену '0' на '1' и наоборот с помощью дополнительной замены
                output_file.writelines(line.replace('0', '#').replace('1', '0').replace('#', '1'))


print(reverse_numbers('const_file.txt'))
