import sys
# sys.stdin = open('2606바이러스.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

def dfs(start):
    visited[start] = 1

    for i in arr[start]:
        if not visited[i]:
            dfs(i)


n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
# print(arr)

for _ in range(m):
    node1, node2 = map(int, input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)

# print(arr)

dfs(1)
# print(visited)
cnt = -1
for j in visited:
    if j == 1:
        cnt += 1

print(cnt)




