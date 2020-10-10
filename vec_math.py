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
    def __init__(self, x: float, y: float):
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
            if isinstance(a, Vec3):
                t = 'vec3'
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
            if isinstance(a, Vec3):
                t = 'vec3'
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
            if isinstance(a, Vec3):
                t = 'vec3'
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
        yield from (self.x, self.y)

    # свойства
    @property
    def size(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def angle(self):
        return acos(dot(self, Vec2(1, 0)) / self.size)

    @property
    def xy(self):
        return Vec2(self.x, self.y)

    @xy.setter
    def xy(self, a):
        if isinstance(a, Vec2):
            self.x, self.y = a.x, a.y

    @property
    def yx(self):
        return Vec2(self.y, self.x)

    @yx.setter
    def yx(self, a):
        if isinstance(a, Vec2):
            self.y, self.x = a.y, a.x


class Vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    # сложение
    def __add__(self, a):
        if isinstance(a, Vec3):
            return Vec3(self.x + a.x, self.y + a.y, self.z + a.z)

        elif isinstance(a, tuple) and len(a) == 3:
            return Vec3(self.x + a[0], self.y + a[1], self.z + a[2])

        else:
            t = ''

            if isinstance(a, str):
                t = 'str'
            if isinstance(a, int):
                t = 'int'
            if isinstance(a, float):
                t = 'float'
            if isinstance(a, Vec2):
                t = 'vec2'
            if isinstance(a, Mat2):
                t = 'mat2'
            if isinstance(a, Mat3):
                t = 'mat3'
            if isinstance(a, Mat4):
                t = 'mat4'

            raise TypeError("unsupported operand type(s) for +: 'vec2' and '" + t + "'")

    # вычитание
    def __sub__(self, a):
        if isinstance(a, Vec3):
            return Vec3(self.x - a.x, self.y - a.y, self.z + a.z)

        elif isinstance(a, tuple) and len(a) == 3:
            return Vec3(self.x - a[0], self.y - a[1], self.z - a[2])

        else:
            t = ''

            if isinstance(a, str):
                t = 'str'
            if isinstance(a, int):
                t = 'int'
            if isinstance(a, float):
                t = 'float'
            if isinstance(a, Vec2):
                t = 'vec2'
            if isinstance(a, Mat2):
                t = 'mat2'
            if isinstance(a, Mat3):
                t = 'mat3'
            if isinstance(a, Mat4):
                t = 'mat4'

            raise TypeError("unsupported operand type(s) for -: 'vec2' and '" + t + "'")

    # умножение
    def __mul__(self, a):
        if isinstance(a, Vec3):
            return Vec3(self.x * a.x, self.y * a.y, self.z * a.z)

        elif isinstance(a, tuple) and len(a) == 3:
            return Vec3(self.x * a[0], self.y * a[1], self.z * a[2])

        elif isinstance(a, int) or isinstance(a, float):
            return Vec3(self.x * a, self.y * a, self.z * a)

        elif isinstance(a, Mat3):
            return Vec3(
                a.mat[0][0] * self.x + a.mat[0][1] * self.y + a.mat[0][2] * self.z,
                a.mat[1][0] * self.x + a.mat[1][1] * self.y + a.mat[1][2] * self.z,
                a.mat[2][0] * self.x + a.mat[2][1] * self.y + a.mat[2][2] * self.z,
            )

        else:
            t = ''

            if isinstance(a, str):
                t = 'str'
            if isinstance(a, Vec2):
                t = 'vec2'
            if isinstance(a, Mat2):
                t = 'mat3'
            if isinstance(a, Mat4):
                t = 'mat4'

            raise TypeError("unsupported operand type(s) for +: 'vec2' and '" + t + "'")

    # вычитание
    def __truediv__(self, a):
        if isinstance(a, Vec3):
            return Vec3(self.x / a.x, self.y / a.y, self.z / a.z)

        elif isinstance(a, tuple) and len(a) == 3:
            return Vec3(self.x / a[0], self.y / a[1], self.z / a[2])

        elif isinstance(a, int) or isinstance(a, float):
            return Vec3(self.x / a, self.y / a, self.z / a)

        else:
            t = ''

            if isinstance(a, str):
                t = 'str'
            if isinstance(a, Vec2):
                t = 'vec2'
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
        yield from (self.x, self.y, self.z)

    # свойства
    @property
    def size(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    @property
    def xy(self):
        return Vec2(self.x, self.y)

    @xy.setter
    def xy(self, a):
        if isinstance(a, Vec2):
            self.x, self.y = a.x, a.y

    @property
    def yx(self):
        return Vec2(self.y, self.x)

    @yx.setter
    def yx(self, a):
        if isinstance(a, Vec2):
            self.y, self.x = a.x, a.y

    @property
    def xz(self):
        return Vec2(self.x, self.z)

    @xz.setter
    def xz(self, a):
        if isinstance(a, Vec2):
            self.x, self.z = a.x, a.y

    @property
    def zx(self):
        return Vec2(self.x, self.z)

    @zx.setter
    def zx(self, a):
        if isinstance(a, Vec2):
            self.z, self.x = a.x, a.y

    @property
    def yz(self):
        return Vec2(self.y, self.z)

    @yz.setter
    def yz(self, a):
        if isinstance(a, Vec2):
            self.y, self.z = a.x, a.y

    @property
    def zy(self):
        return Vec2(self.z, self.y)

    @zy.setter
    def zy(self, a):
        if isinstance(a, Vec2):
            self.z, self.y = a.x, a.y

    @property
    def xyz(self):
        return Vec3(self.x, self.y, self.z)

    @xyz.setter
    def xyz(self, a):
        if isinstance(a, Vec3):
            self.x, self.y, self.z = a.x, a.y, a.z

    @property
    def zyx(self):
        return Vec3(self.z, self.y, self.x)

    @zyx.setter
    def zyx(self, a):
        if isinstance(a, Vec3):
            self.z, self.y, self.x = a.x, a.y, a.z

    @property
    def yxz(self):
        return Vec3(self.y, self.x, self.z)

    @yxz.setter
    def yxz(self, a):
        if isinstance(a, Vec3):
            self.y, self.x, self.z = a.x, a.y, a.z

    @property
    def zxy(self):
        return Vec3(self.z, self.x, self.y)

    @zxy.setter
    def zxy(self, a):
        if isinstance(a, Vec3):
            self.z, self.x, self.y = a.x, a.y, a.z

    @property
    def xzy(self):
        return Vec3(self.x, self.z, self.y)

    @xzy.setter
    def xzy(self, a):
        if isinstance(a, Vec3):
            self.x, self.z, self.y = a.x, a.y, a.z

    @property
    def yzx(self):
        return Vec3(self.y, self.z, self.x)

    @yzx.setter
    def yzx(self, a):
        if isinstance(a, Vec3):
            self.y, self.z, self.x = a.x, a.y, a.z


# ФУНКЦИИ
def dot(a, b):
    v = a * b
    print(v.x, v.y)
    res = 0

    for i in v:
        res += i

    return res


def distance(a, b):
    return len(a - b)


def norm(a):
    return a / a.size
