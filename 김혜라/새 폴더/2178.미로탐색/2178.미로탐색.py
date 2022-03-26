import sys; sys.stdin = open('2178.미로탐색.txt')

from collections import deque

def bfs(x, y):
    que = deque()
    visited = [False for i in range(m) for _ in range(n)]

    que.append(x, y)
    visited[x][y] = True

    while len(que) > 0:
        size = len(que)

        for _ in range(size):
            x, y = que[0][0], que[0][1]
            que.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]




n, m = map(int, input().split())
arr =