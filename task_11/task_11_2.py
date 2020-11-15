class Car(object):

    def __init__(self, mark, model, years_output, speed: int = 0):
        self.__mark = mark
        self.__model = model
        self.__years_output = years_output
        self.__speed = speed

    def more_speed(self):
        self.__speed += 5
        return f'{self.__speed}'

    def less_speed(self):
        self.__speed += -5
        return f'{self.__speed}'

    def stop(self):
        self.__speed = 0
        return f'{self.__speed}'

    def show_speed(self):
        return f'Speed car {self.__speed}!'

    def turn(self):
        self.__speed = -self.__speed
        return f'Reverse speed {self.__speed}'


car = Car(mark='KIA', model='Sportage', years_output='2015 год')

if __name__ == '__main__':
    print(car.more_speed())
    print(car.more_speed())
    print(car.less_speed())
    print(car.stop())
    print(car.more_speed())
    print(car.show_speed())
    print(car.turn())
