from math import pi


class Shape(object):

    def __init__(self, area, perimeter):
        self.__area = 0
        self.__perimeter = 0

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * pi

    def perimeter(self):
        return self.radius * 2 * pi


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4


def main():
    square = Square(5)
    circle = Circle(2)
    print('THE SQUARE AREA IS: ', square.area(), '\n')
    print('THE CIRCLE AREA IS: ', circle.area(), '\n')
    print('THE SQUARE PERIMETER IS: ', square.perimeter(), '\n')
    print('THE CIRCLE PERIMETER IS: ', circle.perimeter(), '\n')


if __name__ == '__main__':
    main()
