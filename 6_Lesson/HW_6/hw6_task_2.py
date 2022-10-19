# Для чисел в пределах от 20 до n найти числа, кратные 20 или 21. Use comprehension.

def my_list(num):
    return [i for i in range(20, num + 1) if i % 20 == 0 or i % 21 == 0]


print(my_list(int(input())))