import sys; sys.stdin = open('섬의개수.txt')
from collections import deque
queue = deque()
def bfs(x, y):
    arr[x][y] = 3
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for nx, ny in ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)):
            nx = x + nx
            ny = y + ny

            if 0<= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                arr[nx][ny] = 3
                queue.append((nx, ny))

    return 1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += bfs(i, j)

    print(cnt)
    # print(arr)












# w = h = 1
# while w != h != 0:
#     w, h = map(int, input().split())
#     if w == h == 0:
#         break
#     arr = [list(map(int, input().split())) for _ in range(h)]
#
#     print(arr)


