a = int(input("введите целое положительное десятичное число......."))
result = ""
while a != 0:
  result = str(a % 2) + result  
  a = a//2
print (result)
