import math
# Линейное уравнение
# ax+b=0 => x=-b/a, когда a!=0

def Linear_equation(a, b):
    if a != 0:
        return [-b / a]
    else: return 'Это уравнение имеет бесконечное количество решений'

# Квадратное уравнение
# ax^2+bx+c=0
# x1=(-b+sqrt(D))/2a, x2=(-b-sqrt(D))/2a, где D=(b^2-4ac) - дискриминант
# если D<0, то у уравнения нет корней
# если D=0, то у уравнения два равных корня
# если D>0, то у уравнения два различных корня

def Quadratic_equation(a, b, c):
    if a == 0: return Linear_equation(b, c)
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        return [-b / (2 * a)]
    elif discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    else: return 'Это уравнение имеет бесконечное количество решений'

# Кубическое уравнение
# ax^3+bx^2+cx+d=0

def Cubic_equation(a, b, c, d):
    if a == 0 and b == 0: return Linear_equation(c, d)
    if a == 0: return Quadratic_equation(b, c, d)
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    Q = (p / 3) ** 3 + (q / 2) ** 2
    if Q > 0:
        alpha = (-q / 2 - math.sqrt(Q)) ** (1 / 3)
        beta = (-q / 2 + math.sqrt(Q)) ** (1 / 3)
        y1 = alpha + beta
        y2 = complex(-(alpha + beta) / 2, (alpha - beta) / 2 * math.sqrt(3))
        y3 = complex(-(alpha + beta) / 2, -(alpha - beta) / 2 * math.sqrt(3))
        return [y1 - b / (3 * a), y2 - b / (3 * a), y3 - b / (3 * a)]
    elif Q == 0:
        alpha = (-q / 2) ** (1 / 3)
        beta = (-q / 2) ** (1 / 3)
        y1 = alpha + beta
        if p == q == 0:
            return [y1 - b / (3 * a)]
        y2 = -(alpha + beta) / 2
        return [y1 - b / (3 * a), y2 - b / (3 * a)]
    else: # формула неверная (нужно по Виету)
        alpha = (-q / 2) ** (1 / 3)
        beta = (-q / 2) ** (1 / 3)
        y1 = alpha + beta
        y2 = -(alpha + beta) / 2
        y3 = -(alpha + beta) / 2
        return [y1 - b / (3 * a), y2 - b / (3 * a), y3 - b / (3 * a)]

# Общий решатель уравнений

def All_equation(a, b, c = None, d = None):
    if c != None and d!= None:
        return Cubic_equation(a, b, c, d)
    if c != None:
        return Quadratic_equation(a, b, c)
    return Linear_equation(a, b)   