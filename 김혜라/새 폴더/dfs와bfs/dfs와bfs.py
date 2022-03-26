import sys; sys.stdin = open('dfs와bfs.txt')
from collections import deque


def dfs(v):
    visited[v] = 1
    # print(visited)
    # print(arr[v])
    print(v, end=' ')

    for i in arr[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited = [0] * (n + 1)
    queue = deque()
    queue.append(v)
    # print(queue)
    visited[v] = 1
    # print(visited)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

#정점의 개수, 간선의 개수, 시작점
n, m, v = map(int, input().split())
first_v = v
arr = [[] for _ in range(n + 1)]
# print(arr)
for _ in range(m):
    node1, node2 = map(int, input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)
# print(arr)
for i in range(len(arr)):
    arr[i] = sorted(arr[i])
# print(arr)

visited = [0] * (n + 1)
# print(visited)
dfs(first_v)
print()
bfs(first_v)


