from sympy import *
import matplotlib.pyplot as plt

interval = list(range(-5, 6))
fx = [-3 * x**2 - 2 * x + 5 for x in interval]
plt.plot(interval, fx)
plt.grid(color='g')
plt.show()

x = Symbol('x')
func = -3 * x**2 - 2 * x + 5

result = list(solve(func, x))
x1 = result[0]
x2 = result[1]
print(f'Корни уравнения: {x1}, {x2}')

derivative = diff(func)
increase = solve(derivative > 0)
decrease = solve(derivative < 0)
print(f'Функция возрастает: {increase}')
print(f'Функция убывает: {decrease}')

topx = list(solve(derivative, x))
topy = func.subs(x, topx[0])
print(f'Вершина функции: [{topx[0]}, {topy}]')

y1 = func.subs(x, x1 - 1)
if y1 > 0: print(f'На промежутке ({-oo}, {x1}) функция > 0')
else: print(f'На промежутке ({-oo}, {x1}) функция < 0')

y2 = func.subs(x, round(x1 + 1))
if y2 > 0: print(f'На промежутке ({x1}, {x2}) функция > 0')
else: print(f'На промежутке ({x1}, {x2}) функция < 0')

y3 = func.subs(x, x2 + 1)
if y3 > 0: print(f'На промежутке ({x2}, {oo}) функция > 0')
else: print(f'На промежутке ({x2}, {oo}) функция < 0')