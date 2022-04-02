import sys
# sys.stdin = open('1012유기농배추.txt')
from pprint import pprint
sys.setrecursionlimit(10**9)


def dfs(y, x):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if arr[y][x]:
        arr[y][x] = 0
        dfs(y + 1, x)
        dfs(y - 1,x)
        dfs(y, x + 1)
        dfs(y, x - 1)
        return True
    return False

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    # pprint(arr)
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    # pprint(arr)

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1
    # pprint(arr)
    print(result)

    # [[0, 0, 0, 0, 1],
    #  [0, 0, 0, 0, 0],
    #  [1, 1, 1, 1, 1]]

    # [[0, 0, 0, 0, 1],
    #  [0, 0, 0, 0, 0],
    #  [0, 0, 0, 1, 1]]


#
# [[0, 0, 0, 0, 1],
#  [0, 0, 0, 0, 0],
#  [1, 1, 1, 1, 1]]

