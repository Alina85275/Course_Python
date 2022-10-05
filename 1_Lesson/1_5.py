a = int(input())
if a % 30 and (a % 5 == 0 and a % 10 == 0 and a % 15 == 0):
     print('yes')
else:
    print('no')