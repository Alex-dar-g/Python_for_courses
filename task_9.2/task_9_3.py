"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка."""
import functools
from typing import Optional


def decorator_for_remove_even_numbers(func):
    """Function for remove even numbers"""
    @functools.wraps(func)
    def search_even_numbers(some_list: list) -> Optional[list]:
        """Search even numbers and remove them"""
        if not isinstance(some_list, list):
            print(f'Вы ввели не список')
            return None
        func(list(filter(lambda element: element % 2 if isinstance(element, int) else None, some_list)))
    return search_even_numbers


@decorator_for_remove_even_numbers
def input_list(list_numbers: list):
    """Input function"""
    print(f"{list_numbers}")


decorator_for_remove_even_numbers(input_list([1, 2, 'dsf', 4, 5, 7, 8]))

