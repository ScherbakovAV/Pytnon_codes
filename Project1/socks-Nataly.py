a, b = map(int, input("введите 2 числа через пробел").split())
if a > b:
    c = b
else:
    c = a
d = (abs(a-b))//2
print(c, d)
