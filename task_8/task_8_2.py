input_string = input()
# Просим ввести пользователя значения через запятую. После сплитим их по запятой.
# Передаём каждый элемент списка в анонимную функцию и умножаем строку на 2
func_lambda = map(lambda string: dict.fromkeys([string * 2]), input_string.split(','))

print(list(func_lambda))
