pupils = [
    {
        'firstname': 'Masha',
        'group': 42,
        'physics': 7,
        'math': 9,
        'history': 6,
    },
    {
        'firstname': 'Sasha',
        'group': 43,
        'physics': 2,
        'math': 10,
        'history': 8,
    },
    {
        'firstname': 'Pasha',
        'group': 13,
        'physics': 5,
        'math': 2,
        'history': 1,
    },
    {
        'firstname': 'Alena',
        'group': 20,
        'physics': 5,
        'math': 9,
        'history': 6,
    },
    {
        'firstname': 'Anjela',
        'group': 28,
        'physics': 6,
        'math': 8,
        'history': 8,
    },
    {
        'firstname': 'Alisa',
        'group': 31,
        'physics': 5,
        'math': 9,
        'history': 6,
    },
    {
        'firstname': 'Andrey',
        'group': 13,
        'physics': 3,
        'math': 8,
        'history': 5,
    },
    {
        'firstname': 'Alesha',
        'group': 30,
        'physics': 3,
        'math': 6,
        'history': 8,
    },
    {
        'firstname': 'Stas',
        'group': 23,
        'physics': 7,
        'math': 9,
        'history': 3,
    },
    {
        'firstname': 'Ilya',
        'group': 24,
        'physics': 7,
        'math': 7,
        'history': 6,
    },

]

length_list_comprehension = len(list(range(0, 10)))
index_list_comprehension = 0
list_comprehension = []

while index_list_comprehension < length_list_comprehension:
    # заносим срезанные значения в список
    list_comprehension.append([values for values in pupils[index_list_comprehension].values()][2:5])
    index_list_comprehension += 1

index_list = 0
index_current_list = 0
length_list = len(list_comprehension)


while index_list < length_list_comprehension:
    # создаём временный список и окрулгяем среднее арифметическое
    current_list = list_comprehension[index_list]
    average_numbers_list = round(sum(current_list)/3, 1)

    # вывод информации об ученике и его средний балл
    if average_numbers_list >= 4:
        print(pupils[index_list]['firstname'], f'- Средний балл: {average_numbers_list}')
    index_list += 1
