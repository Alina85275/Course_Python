# Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
from random import choices

def new_list(size):
    list_of_numbers = choices(range(1, size * 2), k = size)
    return list_of_numbers
n_list = new_list(10)
print(n_list)

def range_nums(new_list: list):
    my_list = []
    for i in range(len(new_list)):
        f = new_list[i]
        lis = [f]
        for x in range(i+1, len(new_list)):
            if new_list[x] >f:
                f = new_list[x]
                lis.append(f)
        if len(lis) > 1:
            my_list.append(lis)
    return my_list
print(range_nums(n_list))
