# Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
n = int(input('Position one '))
s = int(input('Position two '))
k = int(input())
l = []
for i in range(-k,k+1):
    l.append(i)
for i in range (len(l)):
    p = l[n -1] *l[s - 1]
print('-', n, '->', l, '->', p)
