a = int(input("Введите целое положительное десятичное число......."))
b = a
c = a
result_bin = ""
result_oct = ""
result_hex = ""
tmp_hex = ""
while a != 0:
    result_bin = str(a % 2) + result_bin
    a = a//2
while b != 0:
    result_oct = str(b % 8) + result_oct
    b = b//8
while c != 0:
    tmp_hex = c % 16
    if tmp_hex == 10:
        tmp_hex = str("A")
    if tmp_hex == 11:
        tmp_hex = str("B")
    if tmp_hex == 12:
        tmp_hex = str("C")
    if tmp_hex == 13:
        tmp_hex = str("D")
    if tmp_hex == 14:
        tmp_hex = str("E")
    if tmp_hex == 15:
        tmp_hex = str("F")
    result_hex = str(tmp_hex) + result_hex
    c = c//16
print("Это число в двоичной системе счисления: ", result_bin)
print("Это число в восьмеричной системе счисления: ", result_oct)
print("Это число в шестнадцатеричной системе счисления: ", result_hex)
