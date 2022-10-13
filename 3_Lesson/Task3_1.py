# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Наипшите программу, определяющую присютствует ли в заданном списке число, полученное от пользователя.
from random import sample
def num_in_list(count, number):
    if count < 0:
        return "Error"
    mylist = sample(range(1, count *  2), count) # count * 2 - диапазон значений от 1 до 20, count - размер списка (10)
    print(mylist)
    if number in mylist:
        return "YES"
    return "NO"

print(num_in_list(int(input()), int(input())))



