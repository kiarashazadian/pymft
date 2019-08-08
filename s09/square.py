class Area:
    def __get__(self, instance, owner):
        return instance.side ** 2

    def __set__(self, instance, value):

        instance.side = value ** 0.5


class Perimeter:
    def __get__(self, instance, owner):

        return instance.side * 4

    def __set__(self, instance, value):

        instance.side = value / 4


class Square:
    area = Area()
    perimeter = Perimeter()

    def __init__(self, a):
        self.side = a


s = Square(5)
print(s.area)
s.area = 100
print(s.side)