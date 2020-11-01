from lesson12.task_12.main import Triangle, Point, Square, Circle

if __name__ == '__main__':
    triangle = Triangle(Point(2, 4), Point(3, 5), Point(3, 6))
    print(triangle.calculate_perimeter())
    print(triangle.calculate_square())

    square = Square(Point(2, 5), Point(1, 5))
    print(square.calculate_perimeter())
    print(square.calculate_square())

    circle = Circle(Point(2, 2), Point(4, 4))
    print(circle.calculate_perimeter())
    print(circle.calculate_square())
