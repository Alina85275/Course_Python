# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
from math import sqrt
def factorize(x):
    l = []
    for i in range(2, int(sqrt(x))+1):
        while x % i == 0:
            x /= i
            l.append(i)
    print(l)                

factorize(650)
