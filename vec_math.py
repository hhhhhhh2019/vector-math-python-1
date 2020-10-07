from math import acos


# МАТРИЦЫ
class Mat2:
    def __init__(self, a, b):
        self.mat = [
            [a.x, a.y],
            [b.x, b.y]
        ]


class Mat3:
    def __init__(self, a, b, c):
        self.mat = [
            [a.x, a.y, a.z],
            [b.x, b.y, b.z],
            [c.x, c.y, c.z]
        ]


class Mat4:
    def __init__(self, a, b, c, d):
        self.mat = [
            [a.x, a.y, a.z, a.w],
            [b.x, b.y, b.z, b.w],
            [c.x, c.y, c.z, c.w],
            [d.x, d.y, d.z, d.w]
        ]


# ВЕКТОРЫ
class Vec2:
    def __init__(self, x: float = 0, y: float = None):
        if y is None:
            y = x

        self.x, self.y = x, y

    # сложение
    def __add__(self, a):
        if isinstance(a, Vec2):
            return Vec2(self.x + a.x, self.y + a.y)

        elif isinstance(a, tuple) and len(a) == 2:
            return Vec2(self.x + a[0], self.y + a[1])

        else:
            t = ''

            if isinstance(a, str):
                t = 'str'
            if isinstance(a, int):
                t = 'int'
            if isinstance(a, float):
                t = 'float'
            if isinstance(a, Mat2):
                t = 'mat2'
            if isinstance(a, Mat3):
                t = 'mat3'
            if isinstance(a, Mat4):
                t = 'mat4'

            raise TypeError("unsupported operand type(s) for +: 'vec2' and '" + t + "'")

    # вычитание
    def __sub__(self, a):
        if isinstance(a, Vec2):
            return Vec2(self.x - a.x, self.y - a.y)

        elif isinstance(a, tuple) and len(a) == 2:
            return Vec2(self.x - a[0], self.y - a[1])

        else:
            t = ''

            if isinstance(a, str):
                t = 'str'
            if isinstance(a, int):
                t = 'int'
            if isinstance(a, float):
                t = 'float'
            if isinstance(a, Mat2):
                t = 'mat2'
            if isinstance(a, Mat3):
                t = 'mat3'
            if isinstance(a, Mat4):
                t = 'mat4'

            raise TypeError("unsupported operand type(s) for -: 'vec2' and '" + t + "'")
    
    # умножение
    def __mul__(self, a):
        if isinstance(a, Vec2):
            return Vec2(self.x * a.x, self.y * a.y)

        elif isinstance(a, tuple) and len(a) == 2:
            return Vec2(self.x * a[0], self.y * a[1])

        elif isinstance(a, int) or isinstance(a, float):
            return Vec2(self.x * a, self.y * a)
        
        elif isinstance(a, Mat2):
            return Vec2(
                a.mat[0][0] * self.x + a.mat[0][1] * self.y,
                a.mat[1][0] * self.x + a.mat[1][1] * self.y,
            )

        else:
            t = ''

            if isinstance(a, str):
                t = 'str'
            if isinstance(a, Mat3):
                t = 'mat3'
            if isinstance(a, Mat4):
                t = 'mat4'

            raise TypeError("unsupported operand type(s) for +: 'vec2' and '" + t + "'")

    # вычитание
    def __truediv__(self, a):
        if isinstance(a, Vec2):
            return Vec2(self.x / a.x, self.y / a.y)

        elif isinstance(a, tuple) and len(a) == 2:
            return Vec2(self.x / a[0], self.y / a[1])

        elif isinstance(a, int) or isinstance(a, float):
            return Vec2(self.x / a, self.y / a)

        else:
            t = ''

            if isinstance(a, str):
                t = 'str'
            if isinstance(a, Mat2):
                t = 'mat2'
            if isinstance(a, Mat3):
                t = 'mat3'
            if isinstance(a, Mat4):
                t = 'mat4'

            raise TypeError("unsupported operand type(s) for /: 'vec2' and '" + t + "'")

    def __len__(self):
        return self.size

    def __abs__(self):
        return self.size

    def __iter__(self):
        for i in self.xy:
            yield i

    # свойства
    @property
    def size(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def angle(self):
        return acos(dot(self, Vec2(1, 0)) / self.size)

    @property
    def xy(self):
        return self.x, self.y

    @xy.setter
    def xy(self, a):
        if isinstance(a, Vec2):
            self.x, self.y = a.xy

        elif isinstance(a, tuple) and len(a) == 2:
            self.x, self.y = a

    @property
    def yx(self):
        return self.y, self.x

    @yx.setter
    def yx(self, a):
        if isinstance(a, Vec2):
            self.y, self.x = a.yx

        elif isinstance(a, tuple) and len(a) == 2:
            self.y, self.x = a


# ФУНКЦИИ
def dot(a, b):
    v = a * b
    res = 0

    for i in v:
        res += i

    return res


def distance(a, b):
    return len(a - b)


def norm(a):
    return a / a.size
