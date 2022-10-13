# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample
def list_new(count):
    new_list = []
    for i in range(count):
        new_list = sample(range(1, count *  2), count)  
    return new_list

def mult_of_numbers(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list


result = list_new(int(input("Размер массива: ")))
print(result)
print(mult_of_numbers(result))