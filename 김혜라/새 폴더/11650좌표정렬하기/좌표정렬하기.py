import sys; sys.stdin = open('좌표정렬하기.txt')

n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

# print(arr)

arr.sort(key=lambda x:(x[0], x[1]))

# print(arr)
for i in arr:
    print(*i)