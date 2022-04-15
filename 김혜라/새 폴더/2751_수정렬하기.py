import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

# print(arr)
arr.sort()
# print(arr)
for i in arr:
    print(i)


