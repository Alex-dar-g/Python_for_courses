"""
Меры измерения

1) 1,00 дюйм = 2,54 см
2) 1 см = 0,3937 дюйма

3) 1 миля = 1,61 км
4) 1 км = 0,6214 мили

5) 1 анг. фунт = 0,4536 кг
6) 1 кг = 2,2046 анг. фунта

7) 1 унция = 28,35 грамм
8) 1 грамм = 0,035 унции

9) 1 анг. галон = 4,5461 литров
10) 1 литр = 0,22 анг. галлона

11) 1 анг. пинта = 0,5683 литра
12) 1 литр = 1,76 анг. пинт
"""


# 1 функция - дюймы в сантиметры


def interpretation_inch_in_centimeter(inch):
    if inch.isdigit():
        value_of_one_inch_in_centimeter = 2.54
        transformation_in_centimeter = round(value_of_one_inch_in_centimeter * float(inch), 2)
        return f'{inch} дюйм = {transformation_in_centimeter} см'
    else:
        return f'Ошибка, введите только целое положительное число'


# 2 функция - сантиметры в дюймы


def interpretation_centimeter_in_inch(centimeter):
    if centimeter.isdigit():
        value_of_one_centimeter_in_inch = 0.3937
        transformation_in_inch = round(value_of_one_centimeter_in_inch * float(centimeter), 2)
        return f'{centimeter} см = {transformation_in_inch} дюйм'
    else:
        return f'Ошибка, введите только целое положительное число'


# 3 функция - мили в километры


def interpretation_mile_in_km(mile):
    if mile.isdigit():
        value_of_one_mile_in_km = 1.61
        transformation_in_km = round(value_of_one_mile_in_km * float(mile), 2)
        return f'{mile} миль = {transformation_in_km} км'
    else:
        return f'Ошибка, введите только целое положительное число'


# 4 функция - километры в мили


def interpretation_km_in_mile(km):
    if km.isdigit():
        value_of_one_km_in_mile = 0.6214
        transformation_in_mile = round(value_of_one_km_in_mile * float(km), 2)
        return f'{km} км = {transformation_in_mile} миль'
    else:
        return f'Ошибка, введите только целое положительное число'


# 5 функция - фунты в кг


def interpretation_pound_in_kg(pound):
    if pound.isdigit():
        value_of_one_pound_in_kg = 0.4536
        transformation_in_kg = round(value_of_one_pound_in_kg * float(pound), 2)
        return f'{pound} фунт = {transformation_in_kg} кг'
    else:
        return f'Ошибка, введите только целое положительное число'


# 6 функция - кг в фунты


def interpretation_kg_in_pound(kg):
    if kg.isdigit():
        value_of_one_kg_in_pound = 2.2046
        transformation_in_pound = round(value_of_one_kg_in_pound * float(kg), 2)
        return f'{kg} кг = {transformation_in_pound} фунт'
    else:
        return f'Ошибка, введите только целое положительное число'


# 7 функция - унции в граммы


def interpretation_oz_in_gram(oz):
    if oz.isdigit():
        value_of_one_oz_in_gram = 28.35
        transformation_in_gram = round(value_of_one_oz_in_gram * float(oz), 2)
        return f'{oz} унция = {transformation_in_gram} грамм'
    else:
        return f'Ошибка, введите только целое положительное число'


# 8 функция - унции в граммы


def interpretation_gram_in_oz(gram):
    if gram.isdigit():
        value_of_one_gram_in_oz = 0.035
        transformation_in_oz = round(value_of_one_gram_in_oz * float(gram), 2)
        return f'{gram} грамм = {transformation_in_oz} унция'
    else:
        return f'Ошибка, введите только целое положительное число'


# 9 функция - галлон в литры


def interpretation_halon_in_liter(halon):
    if halon.isdigit():
        value_of_one_halon_in_liter = 4.5461
        transformation_in_liter = round(value_of_one_halon_in_liter * float(halon), 2)
        return f'{halon} галон = {transformation_in_liter} литр'
    else:
        return f'Ошибка, введите только целое положительное число'


# 10 функция - литры в галлоны


def interpretation_liter_in_halon(liter):
    if liter.isdigit():
        value_of_one_liter_in_halon = 0.22
        transformation_in_halon = round(value_of_one_liter_in_halon * float(liter), 2)
        return f'{liter} литр = {transformation_in_halon} галон'
    else:
        return f'Ошибка, введите только целое положительное число'


# 11 функция - пинты в литры


def interpretation_pint_in_liter(pint):
    if pint.isdigit():
        value_of_one_pint_in_liter = 0.5683
        transformation_in_liter = round(value_of_one_pint_in_liter * float(pint), 2)
        return f'{pint} пинт = {transformation_in_liter} литр'
    else:
        return f'Ошибка, введите только целое положительное число'


# 12 функция - литры в пинты


def interpretation_liter_in_pint(liter):
    if liter.isdigit():
        value_of_one_liter_in_pint = 1.76
        transformation_in_pint = round(value_of_one_liter_in_pint * float(liter), 2)
        return f'{liter} литр = {transformation_in_pint} пинт'
    else:
        return f'Ошибка, введите только целое положительное число'


commands_functions = ('''
1 - Дюймы в сантиметры.
2 - Сантиметры в дюймы.
3 - Мили в километры.
4 - Километры в мили.
5 - Фунты в килограммы.
6 - Килограммы в фунты.
7 - Унции в граммы.
8 - Граммы в унции.
9 - Галлон в литры.
10 - Литры в галлоны.
11 - Пинты в литры.
12 - Литры в пинты.

0 - Выход из программы.
''')

print(commands_functions)

while True:
    print(f'Вам даны варианты перевода мер.\nВведите цифру нужной вам команды: ')
    user_number = input()
    if user_number.isdigit():
        integer_user_number = int(user_number)
        if integer_user_number <= 12:
            # Выход из программы
            if integer_user_number == 0:
                print('Вы вышли из программы.')
                break

            # 1 вызов функции - перевод дюймов в сантиметры
            elif integer_user_number == 1:
                print('Введите сколько дюймов вы хотите перевести в сантиметры: ')
                number_for_translate = input()
                # проверка вводимых значений
                if number_for_translate.isdigit():
                    print(interpretation_inch_in_centimeter(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 2 вызов функции - перевод сантиметров в дюймы
            elif integer_user_number == 2:
                print('Введите сколько сантиметров вы хотите перевести в дюймы: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_centimeter_in_inch(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 3 вызов функции - перевод мили в километры
            elif integer_user_number == 3:
                print('Введите сколько миль вы хотите перевести в километры: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_mile_in_km(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 4 вызов функции - перевод километры в мили
            elif integer_user_number == 4:
                print('Введите сколько километров вы хотите перевести в мили: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_km_in_mile(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 5 вызов функции - перевод фунтов в килограммы
            elif integer_user_number == 5:
                print('Введите сколько фунтов вы хотите перевести в килограммы: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_pound_in_kg(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 6 вызов функции - перевод килограммов в фунты
            elif integer_user_number == 6:
                print('Введите сколько килограммов вы хотите перевести в фунты: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_kg_in_pound(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 7 вызов функции - перевод унций в граммы
            elif integer_user_number == 7:
                print('Введите сколько унций вы хотите перевести в граммы: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_oz_in_gram(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 8 вызов функции - перевод грамм в унции
            elif integer_user_number == 8:
                print('Введите сколько грамм вы хотите перевести в унции: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_gram_in_oz(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 9 вызов функции - перевод галлонов в литры
            elif integer_user_number == 9:
                print('Введите сколько галлонов вы хотите перевести в литры: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_halon_in_liter(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 10 вызов функции - перевод литров в галлоны
            elif integer_user_number == 10:
                print('Введите сколько литров вы хотите перевести в галлоны: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_liter_in_halon(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 11 вызов функции - перевод пинт в литры
            elif integer_user_number == 11:
                print('Введите сколько пинт вы хотите перевести в литры: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_pint_in_liter(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue

            # 12  вызов функции - перевод литров в пинты
            elif integer_user_number == 12:
                print('Введите сколько литров вы хотите перевести в пинты: ')
                number_for_translate = input()
                if number_for_translate.isdigit():
                    print(interpretation_liter_in_pint(number_for_translate), '\n')
                else:
                    print('Необходимо ввести только целое положительное число', '\n')
                    continue
        else:
            print('Введите число в диапазоне от 0 до 12.', '\n')
    else:
        print('Введите только номер необходимой вам команды!')
        continue
