# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding
with open(r'C:\Users\Alina\Desktop\python\Course_Python\5_Lesson\HW_5\s.txt') as f:
    text = f.read()
encoded_val = rle_encode(text) 
with open('s2.txt', 'a', encoding='utf-8 ') as my_f:
    my_f.write(encoded_val)

