import sys; sys.stdin = open('1012유기농배추.txt')
from pprint import pprint
from collections import deque

queue = deque()

def bfs(x, y):
    arr[x][y] = 3
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for nx, ny in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nx = x + nx
            ny = y + ny

            if 0<= nx < m and 0<= ny < n and arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 3

    return 1




t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    # print(arr)
    for _ in range(k):
        y, x = map(int, input().split())
        # print(x, y)
        arr[x][y] = 1

    # pprint(arr)
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += bfs(i, j)

    print(cnt)
    # pprint(arr)