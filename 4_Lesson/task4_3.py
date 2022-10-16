# Задайте 2 числа. Программа должна находить наименьшее общее кратное этих двух чисел.
from math import gcd
a = int(input('a= '))
b = int(input('b= '))
print((a*b)//gcd(a,b))