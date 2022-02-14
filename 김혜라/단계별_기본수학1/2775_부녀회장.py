t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    arr = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        arr[0][i] = i
print(arr)