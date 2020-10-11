"""Дан список чисел. Вернуть список, где каждый число переведено в строку
[5, 3] -> [‘5’, ‘3’]"""
from typing import Optional


def list_strings(some_list: list) -> Optional[list]:
    if not isinstance(some_list, list):
        print('It is not list')
    modified_list = list(map(lambda element: f'{element}', some_list))
    return modified_list


print(list_strings([1, 2, 3, 4, 5]))
