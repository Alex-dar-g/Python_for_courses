class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure(object):
    def calculate_distance(self, *, first_point: Point, second_point: Point):
        diagonal = ((second_point.x - first_point.x) ** 2 + (second_point.y - first_point.y) ** 2) ** 0.5
        return diagonal

    def calculate_sides_for_triangle(self, *, first_point: Point, second_point: Point, third_point: Point):
        first_side = ((second_point.x - first_point.x) ** 2 + (second_point.y - first_point.y) ** 2) ** 0.5
        second_side = ((third_point.x - first_point.x) ** 2 + (third_point.y - first_point.y) ** 2) ** 0.5
        third_side = ((third_point.x - second_point.x) ** 2 + (third_point.y - second_point.y) ** 2) ** 0.5
        return first_side, second_side, third_side


class Circle(Figure):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def calculate_perimeter(self):
        radius = self.calculate_distance(first_point=self.a, second_point=self.b)
        perimeter = 2 * radius * 3.1415
        return perimeter

    def calculate_square(self):
        radius = self.calculate_distance(first_point=self.a, second_point=self.b)
        square = radius * 3.1415
        return square


class Triangle(Figure):
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        tuple_sides = self.calculate_sides_for_triangle(first_point=self.a, second_point=self.b, third_point=self.c)
        perimeter = sum(tuple_sides)
        return perimeter

    def calculate_square(self):
        tuple_sides = self.calculate_sides_for_triangle(first_point=self.a, second_point=self.b, third_point=self.c)
        semi_perimeter = self.calculate_perimeter() / 2
        square = (semi_perimeter * (semi_perimeter - tuple_sides[0])
                  * (semi_perimeter - tuple_sides[1]) * (semi_perimeter - tuple_sides[2])) ** 0.5
        return square


class Square(Figure):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def calculate_perimeter(self):
        diagonal = self.calculate_distance(first_point=self.a, second_point=self.b)
        perimeter = 2 ** 0.5 * 2 * diagonal
        return perimeter

    def calculate_square(self):
        diagonal = self.calculate_distance(first_point=self.a, second_point=self.b)
        square = diagonal ** 2 / 2
        return square
