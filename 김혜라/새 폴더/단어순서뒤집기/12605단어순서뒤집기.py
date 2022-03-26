import sys; sys.stdin = open('12605단어순서뒤집기.txt')

n = int(input())

for tc in range(1, n+1):
    arr = list(input().split())
    stack = []
    print(f'Case #{tc}:', end=' ')
    for i in range(len(arr)):
        print(arr.pop(), end = " ")
    print()

