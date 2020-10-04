from typing import Optional

wrong_input_data = "Вы ввели не строку"


# функция для переворачивания строки
def reverse_input_string(
        string: str,
        wrong_input: str = wrong_input_data
) -> Optional[str]:
    # проверка вводимых данных, чтобы они являлась строкой
    if not isinstance(string, str):
        print(wrong_input)
        return None
    return string[::-1]


input_list = ["поп", "рок", "кино"]
word_not_palindrom = "Это слово не полиндром"
word_true_palindrom = "Это слово полиндром"


# функция для проверки списка на наличие полиндрома
def check_palindrom(
        input_data: list,
        message_wrong_input: str = wrong_input_data,
        message_word_not_palindrom: str = word_not_palindrom,
        message_word_true_palindrom: str = word_true_palindrom,
) -> Optional[str]:
    # првоерка вводимых данных чтобы они являлись списком
    if not isinstance(input_data, list):
        print(message_wrong_input)
        return None

    # сравниваем каждый элемент списка с его :перевёртышем"
    for string_ in input_data:
        if not string_ == reverse_input_string(string_):
            print(message_word_not_palindrom)
            return None
        else:
            print(message_word_true_palindrom)
            return string_


print(check_palindrom(input_list))
