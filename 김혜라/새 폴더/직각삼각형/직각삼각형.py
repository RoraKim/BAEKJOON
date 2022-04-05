import sys; sys.stdin = open('직각삼각형.txt')

while True:
    arr = list(map(int, input().split()))
    # print(arr)
    arr.sort()
    a, b, c = arr
    if a == b == c == 0:
        break

    if c **2 == a**2 + b**2:
        print('right')

    else:
        print('wrong')

    # print(a, b, c)

