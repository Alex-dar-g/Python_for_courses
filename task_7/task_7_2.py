from typing import Optional

input_string = input("Введите только буквы")
wrong_input_data = "Ошибка"


def letters(
        some_input_string: str,
        message_wrong_input: str = wrong_input_data
) -> Optional[dict]:
    # check some_input_string
    if not some_input_string.isalpha():
        print(message_wrong_input)
        return None

    count_for_small_letters = 0
    count_for_upper_letters = 0
    # check some_input_string through cycle for
    for element in some_input_string:
        if element.islower():
            count_for_small_letters += 1
        else:
            count_for_upper_letters += 1

    dictionary_for_count_letters = {
        "Quantity small letters": count_for_small_letters,
        "Quantity upper letters": count_for_upper_letters
    }
    return dictionary_for_count_letters


print(letters(input_string))
