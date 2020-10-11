"""Написать декоратор, который будет выводить время
выполнения функции"""
import time
import functools


def decorator_for_count_time(func):
    """Decorator count time"""
    @functools.wraps(func)
    def count_time(some):
        """Function for calculating the execution time"""
        start_time = time.time()
        func(some)
        print(f"{time.time() - start_time} seconds")
        return None
    return count_time


@decorator_for_count_time
def some_func(something):
    """Working function"""
    print(f"{something}")


decorator_for_count_time(some_func("dsfd"))
