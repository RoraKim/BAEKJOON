import sys
sys.stdin = open('2644_촌수계산.txt')
from collections import deque
# input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]

visited = [0] * (n + 1)

def bfs(start):
    visited[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for i in arr[cur]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[cur] + 1
                print(visited)


for _ in range(m):
    node1, node2 = map(int, input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)

print(arr)



bfs(a)
# print(visited)

print(visited[b] - 1 if visited[b] >0 else -1)



bfs(b)
# print(visited)
# print(visited[a] if visited[a] >0 else -1)


