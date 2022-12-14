# Найдитекорни квадратного уравнения Ах^2 + Вх + С = 0, с помощью модуля. 
# Запросите значения А В С 3 раза. Уравнения и корни запишите в файл.
from math import sqrt
def sqr_r(a, b, c):
    d = b ** 2 - 4 * a * c
    if a == 0:
        return 'error'
    with open('sqr.txt', 'a', encoding='utf-8 ') as my_f:
        my_f.write(f'{a}х^2 + {b}х + {c} = 0\n')
        if d > 0:
            my_f.write(f'{(-b + sqrt(d))/ (2 * a)}\n')
            my_f.write(f'{(-b - sqrt(d))/ (2 * a)}\n')
        elif d == 0:
            my_f.write(f'{-b / (2 * a)}\n')
        else:
            my_f.write('Нет корней\n')



for i in range(3):
    sqr_r(int(input('a: ')), int(input('b: ')), int(input('c: ')))