"""Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный."""
import functools


def decorator_for_reverse_function_arguments(function):
    """Function for reverse arguments function"""
    @functools.wraps(function)
    def reverse_arguments(*args):
        """Do reverse arguments"""
        function(*args[::-1])
    return reverse_arguments


@decorator_for_reverse_function_arguments
def some_function(*args):
    """Input function"""
    print(*args)
    return None


decorator_for_reverse_function_arguments(some_function(1, 2, 'dsf', 4, 5, 7, 8, 'sdf'))
