"""
Задание 10.09
Использовать результаты 10.8. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в task_10_09.py.
1) Создать функцию подсчета полной суммы всех товаров.
2) Создать функцию поиска самого дорогого товара.
3) Создать функцию самого дешевого товара.
4) Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""
from lesson10.task_10_08_and_10_09.csv_utils import sum_all_products, search_most_price, search_less_price,\
    remove_string

# 7 function
print(sum_all_products("new_file_for_record_by_position.csv"))

# 8 function
print(search_most_price("new_file_for_record_by_position.csv"))

# 9 function
print(search_less_price("new_file_for_record_by_position.csv"))

# 10 function
remove_string("new_file_for_record_by_position.csv")
