class House(object):
    def __init__(self, city, width, height):
        self.__city = city
        self.__width = width
        self.__height = height

    @property
    def city(self):
        return f'{self.__city}'

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def width(self):
        return f'{self.__width}'

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return f'{self.__height}'

    @height.setter
    def height(self, height):
        self.__height = height

    def property(self):
        return f'Свойства дома: {self.__height}, {self.__width} '

    def live(self):
        return f'Я живу в {self.__city}'


class Cat(object):
    def __init__(self, color, speed, sleep):
        self.__color = color
        self.__speed = speed
        self.__sleep = sleep

    @property
    def color(self):
        return f'{self.__color}'

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def speed(self):
        return f'{self.__speed}'

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def sleep(self):
        return f'{self.__sleep}'

    @sleep.setter
    def sleep(self, sleep):
        self.__sleep = sleep

    def lazy(self):
        return f'Мой кот спит в среднем: {self.__sleep}'

    def color_my_cat(self):
        return f'Цвет моего кота: {self.__color}'


class Family(object):
    def __init__(self, quantity, middle_age, medium_height):
        self.__quantity = quantity
        self.__middle_age = middle_age
        self.__medium_height = medium_height

    @property
    def quantity(self):
        return f'{self.__quantity}'

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def middle_age(self):
        return f'{self.__middle_age}'

    @middle_age.setter
    def middle_age(self, middle_age):
        self.__middle_age = middle_age

    @property
    def medium_height(self):
        return f'{self.__medium_height}'

    @medium_height.setter
    def medium_height(self, medium_height):
        self.__medium_height = medium_height

    def quantity_people_in_my_family(self):
        return f'Наша семья состоит из: {self.__quantity}'

    def age_my_family(self):
        return f'Средний возраст семьи: {self.__middle_age}'


class Children(object):
    def __init__(self, quantity, middle_age, education):
        self.__quantity = quantity
        self.__middle_age = middle_age
        self.__education = education

    @property
    def quantity(self):
        return f'{self.__quantity}'

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def middle_age(self):
        return f'{self.__middle_age}'

    @middle_age.setter
    def middle_age(self, middle_age):
        self.__middle_age = middle_age

    @property
    def education(self):
        return f'{self.__education}'

    @education.setter
    def education(self, education):
        self.__education = education

    def children(self):
        return f'У нас в семье: {self.__quantity} детей'

    def age_children(self):
        return f'Средний возраст детей: {self.__middle_age}'


class Fox(object):
    def __init__(self, color, trick, speed):
        self.__color = color
        self.__trick = trick
        self.__speed = speed

    @property
    def color(self):
        return f'{self.__color}'

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def trick(self):
        return f'{self.__trick}'

    @trick.setter
    def trick(self, trick):
        self.__trick = trick

    @property
    def speed(self):
        return f'{self.__speed}'

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def trick_fox(self):
        return f'Лисы для выживания используют: {self.__trick}'

    def life_fox(self):
        return f'Лисы очень хорошо охотяться и развивают скорость до: {self.__speed}'


house = House(city='Minsk', width='15m', height='10m')
cat = Cat(color='gray', sleep='14', speed='20 км/ч')
family = Family(quantity='5', middle_age='40 лет', medium_height='170 см')
children = Children(quantity='3', middle_age='30 лет', education='Все образованы')
fox = Fox(color='rufous', speed='25 км/ч', trick='хитрость')

if __name__ == '__main__':
    
    # class House
    print(house.city)
    house.city = 'Vitebsk'
    print(house.city)
    print(house.height)
    print(house.width)
    # методы класса
    print(house.property())
    print(house.live())

    # class Cat
    print(cat.speed)
    print(cat.color)
    print(cat.sleep)
    # методы класса
    print(cat.lazy())
    print(cat.color_my_cat())

    # class Family
    print(family.quantity)
    print(family.middle_age)
    print(family.medium_height)
    # методы класса
    print(family.quantity_people_in_my_family())
    print(family.age_my_family())

    # class Children
    print(children.middle_age)
    print(children.quantity)
    print(children.education)
    # методы класса
    print(children.children())
    print(children.age_children())

    # class Fox
    print(fox.color)
    print(fox.speed)
    print(fox.trick)
    # методы класса
    print(fox.life_fox())
    print(fox.trick_fox())
