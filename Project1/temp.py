import Socks
import math
# a * x ^ 2 - b = 0
# x = sqrt(b / a)

a = 5
b = 12
if a > 0:
    x = math.sqrt(b / a)
    print("Корень квадратного уравнения a*x^2-b=0 при a = " + str(a) + ", b = " + str(b) + " равен " + str(round(x, 2)))
else:
    print("Корня у данного уравнения нет")

# a * x ^ 3 - b = 0
# x = (b / a) ^ (1 / 3)
if a > 0:
    x = math.pow(b / a, 1 / 3)
    print("Корень кубического уравнения a*x^3-b=0 при a = " + str(a) + ", b = " + str(b) + " равен " + str(x))
else:
    print("Корня у данного уравнения нет")


