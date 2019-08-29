class Area:
    def __get__(self, instance, owner):
        return instance.width * instance.height

    def __set__(self, instance, value):
        ratio = (value / instance.area) ** 0.5
        instance.width *= ratio
        instance.hight *= ratio


class Perimeter:
    def __get__(self, instance, owner):
        return (instance.width + instance.height) * 2

    def __set__(self, instance, value):
        ratio = (value / instance.area)
        instance.width *= ratio
        instance.hight *= ratio


class Rectangle:
    area = Area()
    perimeter = Perimeter()

    def __init__(self, w, h):
        self.width = w
        self.height = h


class Square(Rectangle):
    """
    >>> s = Square(2.0)
    >>> s.area
    4.0
    >>> s.perimeter = 16.0
    >>> s.area
    16.0
    """

    def __init__(self, a):
        super().__init__(a, a)


if __name__ == '__main__':
    import doctest

    doctest.testmod()