# Просим пользователя ввести значения через запятую, после сплитим их для списка
list_strings = iter(input().split(','))
# Счётчик сделан для вывода порядкового элемента
index = 0

for string in list_strings:
    # После проверяем в цикле значение каждого элемента на строку
    if not isinstance(string, str):
        continue
    print(f'{index} - {string}')
    index += 1
