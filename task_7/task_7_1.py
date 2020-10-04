from typing import Optional
from numpy import unique

input_list = [0, 1, 2, 4, 1, 5, 1, 1, 0, 6, 2]
warning_message = "Это не список"
true_list = "Вот это уникальный список"


def unique_list(
        some_list: list,
        message_wrong_input: str = warning_message,
        message_true_input: str = true_list,
) -> Optional[list]:
    if not isinstance(some_list, list):
        print(message_wrong_input)
        return None
    unique_input_list = [number for number in unique(some_list)]
    print(message_true_input)
    return unique_input_list


print(unique_list(input_list))
