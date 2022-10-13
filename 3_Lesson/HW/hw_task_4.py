# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import uniform
def list_new(count):
    new_list = []
    for i in range(count):
        k = round(uniform(3, 99), 2)
        n = round((k % 1), 2)
        new_list.append(n)
    return new_list

def diff_max_min(mylist):
    max1 = -1
    min1 = 1
    for i in range(len(mylist)):
        if mylist[i]> max1:
            max1=mylist[i]
        if mylist[i] < min1:
            min1 = mylist[i]
    print('min = ', min1, 'max = ', max1, 'differece = ', max1-min1)


result = list_new(int(input("Размер массива ")))
print(result)
print(diff_max_min(result))
