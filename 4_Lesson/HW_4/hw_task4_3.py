# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
import random 
def in_number_list(count):
    if count < 0:
        print('Negative value of the number of numbers!')
    L = list()
    for _ in range(count):
        L.append(random.randint(0, count))
    print(L)
    list_copy = []
    for x in L:
        if x not in list_copy:
            list_copy.append(x)
    print(list_copy)
in_number_list(-1)

