"""
Задание 10.07
Создать матрицу случайных чисел и сохранить ее в json
файл. После прочесть ее, обнулить все четные элементы
и сохранить в другой файл
"""
import numpy as np
import json


# построение и запись матрицы в json
def construction_matrix(size_matrix: str):
    """
        Function for create matrix n*n
    """
    if not size_matrix.isdigit():
        return f"Введите число"
    integer_size_number = int(size_matrix)
    # создание матрицы n*n
    random_matrix = np.arange(integer_size_number ** 2).reshape(integer_size_number, integer_size_number)
    array_matrix = np.array(random_matrix).tolist()
    # запись данный в json
    json_data = {'matrix': array_matrix}
    with open('data_file.json', 'w') as data_file:
        json.dump(json_data, data_file)


# просим пользователя ввести размер матрицы
num = input('Введите размер матрицы, который вы хотите создать: ')
construction_matrix(num)


# замена чётных элементов в матрице на 0 и запись матрицы в json
def output_matrix_in_file(name_file: str):
    """
        Function for reverse even elements in matrix
    """
    # чтение файла
    with open(name_file, 'r') as data_file:
        data = json.load(data_file)
        # преобразовываем матрицу в массив и заменяем элементы
        data_matrix = np.array(data['matrix'])
        np.putmask(data_matrix, data_matrix % 2 == 0, 0)
    # преобразование матрицы из массива в список
    array_data_matrix = np.array(data_matrix).tolist()
    json_data = {'matrix': array_data_matrix}
    with open('reverse_elements.json', 'w') as output_file:
        json.dump(json_data, output_file)


output_matrix_in_file('data_file.json')
