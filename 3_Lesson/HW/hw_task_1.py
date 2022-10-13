# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in  5
# out [10, 2, 3, 8, 9]
# 22
from random import sample
def list_new(count):
    new_list = []
    for i in range(count):
        new_list = sample(range(1, count *  2), count)  # k - количество букв
    return new_list

def sum_elements(mylist):
    sum = 0
    for i in range(0, len(mylist), 2):
        sum = sum + mylist[i]
    print(sum)

result=list_new(5)
print(result)
sum_elements(result)
