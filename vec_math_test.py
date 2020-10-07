from math import cos, sin, pi
from vec_math import *

a = Vec2(1, 0) * Mat2(
    Vec2(cos(pi), -sin(pi)),
    Vec2(sin(pi), cos(pi)),
)

print(a.angle, a.xy)
