# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +-/* приотритет операций стандартный.
# *Добавьте скобки, приоритет операций меняется. -2 + (4 / 2 -7 + 8 * 7) * 3
actions = {
    '^': lambda x, y: str(float(x) ** float(y)),
    '*': lambda x, y: str(float(x) * float(y)),
    '/': lambda x, y: str(float(x) / float(y)),
    '+': lambda x, y: str(float(x) + float(y)),
    '-': lambda x, y: str(float(x) - float(y))
}

first_test = "-2 + ( 4 / ( 2 - 7 ) + 8 * 7 ) * 3"

def find_proirity(numbers: list):
    new_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] == '(':
            if '(' in numbers[i+1:]:
                numbers = numbers[:i + 1] + find_proirity(numbers[i+1:])
            g = numbers.index(')', i)
            new_numbers.append(numbers[i+1:g])
            i = g
        else:
            new_numbers.append(numbers[i])
        i += 1
    return new_numbers
changed_list = find_proirity(first_test.split())
print(changed_list)

def calc(numbers: list):
    for i, num in enumerate(numbers):
        if isinstance(num, list):
            numbers[i] = calc(num)
    new_list = [x for x, sym in enumerate(numbers) if sym in '*/']
    while new_list:
        k = new_list[0]
        a, b, c = numbers[k-1:k+2]
        numbers.insert(k-1, actions[b](a,c))
        del numbers[k,k+3]
        new_list = [x for x, sym in enumerate(numbers) if sym in '*/']
    while len(numbers > 1):
        a, b, c = numbers[:3]
        del numbers[:3]
        numbers.insert(0, actions[b](a,c))
    return numbers[0]

print(calc(changed_list))


