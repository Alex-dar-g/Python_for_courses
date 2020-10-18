"""
    Библиотека для работы с CSV файлами
"""

__all__ = [
    'read_csv_file',
    'write_in_csv_file',
    'adding_a_default_entry',
    'adding_a_record_by_position',
    'remove_a_default_entry',
    'remove_a_record_by_position',
    'sum_all_products',
    'search_most_price',
    'search_less_price',
    'remove_string'
]

import csv
import pandas
from typing import Optional

filed_names = ['product name', 'price(руб)', 'quantity(кг)', 'comment']
warning_message_for_check_str = "Введённый тип данных не является буквами"
warning_message_for_check_int = "Введённый тип данных не является числом"
warning_message_for_name_file = "Введите имя файла"


# функции 1-6 работают под словия задачи № 10.08
# 1 Функция для чтения файла
def read_csv_file(name_file: str):
    """
        Function for read and write csv file
    """
    # проверка имени файла
    if not isinstance(name_file, str):
        print(warning_message_for_name_file)

    # создание файла с начальными данными
    with open(name_file, 'w') as file_csv:
        file = csv.writer(file_csv)
        file.writerow(filed_names)


# 2 Функция для записи в файл
def write_in_csv_file(name_file: str):
    """
        Function for write information in csv file
    """
    if not isinstance(name_file, str):
        print(warning_message_for_name_file)

    # Запись const данных в файл
    with open(name_file, 'a') as w_file:
        data = csv.writer(w_file)
        data.writerow(["морковь", "3р", "4кг", "свежая"])


# 3 Функция для добавления записи в файл по умолчанию
def adding_a_default_entry(name_file: str):
    """
        Function for write information in csv file across input
    """
    if not isinstance(name_file, str):
        print(warning_message_for_name_file)

    # просим ввести пользователя данные, которые он хочет занести в файл
    product_name = input("Введите название продукции: ")
    price = input("Введите цену продукта в рублях: ")
    quantity = input("Введите количество продукта в кг: ")
    comment = input("Введите коментарий к продукту: ")

    # делаем проверку, чтобы строка состола из букв
    if not product_name.isalpha() or not comment.isalpha():
        print(warning_message_for_check_str)
    # делаем проверку, чтобы строка состола из цифр
    if not price.isdigit() or not quantity.isdigit():
        print(warning_message_for_check_int)

    with open(name_file, 'a') as w_r_file:
        data = csv.writer(w_r_file)
        data.writerow([product_name, price, quantity, comment])


# 4 Функция для добавления записи в файл по позиции
def adding_a_record_by_position(name_file: str):
    """
        Function for write information in csv file across input
    """
    if not isinstance(name_file, str):
        print(warning_message_for_name_file)

    # просим ввести пользователя данные, которые он хочет занести в файл
    product_name = input("Введите название продукции: ")
    price = input("Введите цену продукта в рублях: ")
    quantity = input("Введите количество продукта в кг: ")
    comment = input("Введите коментарий к продукту: ")
    index_row = input("Введите номер строки, куда вы хотите записать данные: ")

    # делаем проверку, чтобы строка состола из букв
    if not product_name.isalpha() and not comment.isalpha():
        print(warning_message_for_check_str)
    # делаем проверку, чтобы строка состола из цифр
    if not price.isdigit() and not quantity.isdigit() and not index_row.isdigit():
        print(warning_message_for_check_int)

    # чтение файла и запись данных в словарь
    input_data = [product_name, price, quantity, comment]
    data_list = []
    with open(name_file, 'r') as w_file:
        data = csv.reader(w_file)
        for row in data:
            data_list.append(row)
    # создание нового файла и запись в него изменнёных данных
    with open('new_file_for_record_by_position.csv', 'w') as new_file_csv:
        data_new_file = csv.writer(new_file_csv)
        data_list.insert(int(index_row), input_data)
        for line in data_list:
            data_new_file.writerow(line)


# 5 Функция для удаления записи из файла по умолчанию
def remove_a_default_entry(name_new_file: str):
    """
        Function remove a default entry
    """
    if not isinstance(name_new_file, str):
        print(warning_message_for_name_file)
    # читаем новый файл и заносим данные в список
    data_list = []
    with open(name_new_file, 'r') as r_file:
        data = csv.reader(r_file)
        for line in data:
            data_list.append(line)
    # удаление последней строки из списка
    data_list.pop()
    # создаём новый файл и заносим данные без последней строчки
    with open('new_file_without_last_line.csv', 'w') as new_file:
        new_file_without_last_line = csv.writer(new_file)
        for line in data_list:
            new_file_without_last_line.writerow(line)


# 6 Функция для удаления записи из файла по позиции
def remove_a_record_by_position(name_new_file: str):
    """
        Function remove entry by position
    """
    if not isinstance(name_new_file, str):
        print(warning_message_for_name_file)

    # читаем новый файл и заносим данные в список
    data_list = []
    with open(name_new_file, 'r') as r_file:
        data = csv.reader(r_file)
        for line in data:
            data_list.append(line)
    # просим пользователя ввести номер строки для удаления этой записи и делаем проверку вводимых данных
    user_selection = input("Введите номер строки, которую вы хотите удалить: ")
    if not user_selection.isdigit():
        print(warning_message_for_check_int)
    # удаление последней строки из списка
    data_list.pop(int(user_selection))
    # создаём новый файл и заносим данные без последней строчки
    with open('new_file_without_positional_line.csv', 'w') as new_file:
        new_file_without_last_line = csv.writer(new_file)
        for line in data_list:
            new_file_without_last_line.writerow(line)


# Функции 7 - 10 будут использоваться для работы над задачей № 10.09
# 7 Функция для суммы всех цен
def sum_all_products(name_file: str) -> Optional[int]:
    """
            Function sum all price products
        """
    if not isinstance(name_file, str):
        print(warning_message_for_name_file)
    # чтение файла через пандас и вывод суммы всех цен
    with open(name_file, 'r') as const_file:
        file = pandas.read_csv(const_file)
        sum_product = file['price(руб)'].sum()
    return sum_product


# 8 Функция для поиска самого дорого товара
def search_most_price(name_file: str):
    """
        Function search most price product
    """
    if not isinstance(name_file, str):
        print(warning_message_for_name_file)
    # чтение файла через пандас и вывод строки с наибольшей стоимостью товара
    with open(name_file, 'r') as const_file:
        file = pandas.read_csv(const_file)
        most_price = file.nlargest(1, ['price(руб)'])
    return most_price


# 9 Функция для поиска самого дешёвого товара
def search_less_price(name_file: str):
    """
        Function search less price product
    """
    if not isinstance(name_file, str):
        print(warning_message_for_name_file)
    # чтение файла через пандас и вывод строки с наименьшей стоимостью товара
    with open(name_file, 'r') as const_file:
        file = pandas.read_csv(const_file)
        less_product = file.nsmallest(1, ['price(руб)'])
    return less_product


# 10 Функция для удаления строк в диапазоне
def remove_string(name_file: str):
    """
        Function for search and remove strings
    """
    if not isinstance(name_file, str):
        print(warning_message_for_name_file)
    # запрашиваем у пользователя диапазон строк, которые нужно удалить и проверяем их
    start_line = input('Введите номер строки от которой будут удаляться данные: ')
    end_line = input('Введите номер строки до которой будут удаляться данные: ')
    if not start_line.isdigit() or not end_line.isdigit():
        print(warning_message_for_check_int)
    # преобразовываем данные в числа
    first_number, second_number = int(start_line), int(end_line)
    # чтение файла через пандас и удаление строк в диапазоне
    with open(name_file, 'r') as const_file:
        file = pandas.read_csv(const_file)
        # создание другого файла уже без удалённых строк
        with open('file_without_remove_strings.csv', 'w') as file_without_strings:
            data_without_string = file.drop(file.index[first_number:second_number])
            data_without_string.to_csv(file_without_strings, index=False)


remove_string("new_file_for_record_by_position.csv")
