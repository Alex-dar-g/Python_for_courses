"""
Задание 10.08
Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
записи(по позиции, по-умолчанию последнюю).
В файле task_10_08_and_10_09 импортировать функции. С помощью функций создать
файл с информацией о товарах(Имя товара, цена, количество,
комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""


from lesson10.task_10_08_and_10_09.csv_utils import read_csv_file, write_in_csv_file, adding_a_default_entry,\
    adding_a_record_by_position, remove_a_default_entry, remove_a_record_by_position

# 1 function
read_csv_file("product.csv")

# 2 function
write_in_csv_file("product.csv")

# 3 function
adding_a_default_entry("product.csv")

# 4 function
adding_a_record_by_position("product.csv")

# 5 function
remove_a_default_entry("new_file_for_record_by_position.csv")

# 6 function
remove_a_record_by_position("new_file_for_record_by_position.csv")
