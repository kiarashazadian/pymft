x = 2
y = "b"
z = 3


def its_triangle(a, b, c):
    if not isinstance(a and b and c, int):
        raise TypeError
    if a + b > c and a + c > b and c + b > a:
        print(True)
    else:
        print(False)


def its_Equilateral(a, b, c):
    if not isinstance(a and b and c, int):
        raise TypeError
    if a == b and b == c and a == c:
        print(True)
    else:
        print(False)


try:
    its_triangle(x, y, z)
except:
    print("some thing wrong")
