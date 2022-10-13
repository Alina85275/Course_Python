# Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке либо сообщит, что её нет.
from random import choices
def list_new(count, word):
    new_list = []
    for i in range(count):
        a = choices(word,k=3)  # k - количество букв
        new_list.append(''.join(a))
    return new_list

def list_search(mylist, key):
    if mylist.count(key) > 1:
        print("YES")
        n = mylist.index(key)
        print(mylist.index(key,n+1))
    else:
        print(-1)

result=list_new(45, "abc")
print(result)
list_search(result, input())