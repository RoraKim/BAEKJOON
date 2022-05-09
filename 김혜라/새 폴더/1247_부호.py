import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    summ = 0
    for i in range(n):
        num = int(input())
        summ += num

    if summ == 0:
        print('0')

    elif summ >0:
        print('+')

    else:
        print('-')