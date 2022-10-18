# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
#авб бав вба бав вба

# in
# Number of words: -1
# out
# The data is incorrect
from random import sample
def list_new(count, word):
    if count == -1:
        print("The data is incorrect")
    new_list = []
    for i in range(count):
        a = sample(word,k=3)  # k - количество букв
        new_list.append(''.join(a))
    return new_list
result=list_new(10, "абв")
print(result)

def del_povtor(my_list):
    while 'абв' in my_list:
        my_list.remove('абв')
    print(my_list)

del_povtor(result)

