"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени.
"""


class MyTime(object):
    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    # метод сравнения ==
    def __eq__(self, other):
        return all([
            self.hours == other.hours,
            self.minutes == other.minutes,
            self.seconds == other.seconds,
        ])

    # метод +
    def __add__(self, other):
        # создадим переменную для дней, если будет больше 24 часов
        day = 0
        sum_hours = self.hours + other.hours
        sum_minutes = self.minutes + other.minutes
        sum_seconds = self.seconds + other.seconds
        if sum_hours >= 24:
            day += 1
            sum_hours -= 24
        else:
            pass

        if sum_minutes >= 60:
            sum_hours += 1
            sum_minutes -= 60
        else:
            pass

        if sum_seconds >= 60:
            sum_minutes += 1
            sum_seconds -= 60
        else:
            pass
        return f'{day}:{sum_hours}:{sum_minutes}:{sum_seconds}'

    # метод -
    def __sub__(self, other):
        day = 1
        sub_hours = self.hours - other.hours
        sub_minutes = self.minutes - other.minutes
        sub_seconds = self.seconds - other.seconds

        if sub_hours < 0:
            day -= 1
            # + потому что числа отрицательные
            sub_hours = 24 + sub_hours
        else:
            pass

        if sub_minutes < 0:
            sub_hours -= 1
            sub_minutes = 60 - sub_minutes
        else:
            pass

        if sub_seconds < 0:
            sub_minutes -= 1
            sub_seconds = 60 + sub_seconds
            # если минут меньше 0, то отнимаем один час и минут становится 60
            if not sub_minutes > 0:
                sub_minutes = 60 + sub_minutes
                sub_hours -= 1
            # если часов меньше 0, то отнимаем один день и прибавляем 24 часа
            if not sub_hours > 0:
                sub_hours = 24
        else:
            pass

        return f'{day}:{sub_hours}:{sub_minutes}:{sub_seconds}'

    # метод !=
    # выдаёт True, если все данные разные
    def __ne__(self, other):
        return all([
            self.hours != other.hours,
            self.minutes != other.minutes,
            self.seconds != other.seconds,
        ])

    # метод <=
    # выдаёт True, если все первые входные данные меньше либо равно второго
    def __le__(self, other):
        return all([
            self.hours <= other.hours,
            self.minutes <= other.minutes,
            self.seconds <= other.seconds,
        ])

    # метод >=
    # выдаёт True, если все первые входные данные больше либо равно второго
    def __ge__(self, other):
        return all([
            self.hours >= other.hours,
            self.minutes >= other.minutes,
            self.seconds >= other.seconds,
        ])

    # метод <
    # выдаёт True, если все первые входные данные меньше второго
    def __lt__(self, other):
        return all([
            self.hours < other.hours,
            self.minutes < other.minutes,
            self.seconds < other.seconds,
        ])

    # метод >
    # выдаёт True, если все первые входные данные больше второго
    def __gt__(self, other):
        return all([
            self.hours > other.hours,
            self.minutes > other.minutes,
            self.seconds > other.seconds,
        ])


if __name__ == '__main__':
    my_time_1 = MyTime(18, 50, 55)
    my_time_2 = MyTime(13, 20, 25)

    print(my_time_1 == my_time_2)
    print(my_time_1 + my_time_2)
    print(my_time_2 - my_time_1)
    print(my_time_1 != my_time_2)
    print(my_time_1 <= my_time_2)
    print(my_time_1 >= my_time_2)
    print(my_time_1 < my_time_2)
    print(my_time_1 > my_time_2)
