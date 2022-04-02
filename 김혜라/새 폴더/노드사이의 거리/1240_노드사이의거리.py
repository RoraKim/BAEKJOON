import sys
from pprint import pprint
# sys.stdin = open('1240_노드사이의거리.txt')
from collections import deque
input = sys.stdin.readline

#
# def bfs(start, end):
#     q = deque()
#     q.append(start)
#     visit = [-1] * (N + 1)
#     visit[start] = 0
#     while q:
#         cur = q.popleft()
#         if cur == end: break
#         for adj_node, adj_dist in link_arr[cur]:
#             #방문한적이 있다는 뜻
#             if visit[adj_node] > -1: continue
#             #방문한적이 없는 애들만 q에 넣는다
#             #visited에 거리를 추가
#             visit[adj_node] = visit[cur] + adj_dist
#             q.append(adj_node)
#             print(visit)
#     return visit[end]



def bfs(start, end):
    visit = [0] * (n + 1)
    visit[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        if cur == end:
            break

        for nd2, dist in link_arr[cur]:
            if not visit[nd2]:
                # print(dist)
                visit[nd2] = visit[cur] + dist
                queue.append(nd2)

    # print(visit)
    return visit[cur] - 1


n, m = map(int, input().split())
link_arr = [list() for _ in range(n + 1)]

for _ in range(n-1):
    node1, node2, dis = map(int, input().split())
    link_arr[node1].append((node2, dis))
    link_arr[node2].append((node1, dis))

# print(link_arr)

for _ in range(m):
    start, end = map(int, input().split())
    print(bfs(start, end))




















# for _ in range(N - 1):
#     n1, n2, w = map(int, input().split())
#     link_arr[n1].append((n2, w))
#     link_arr[n2].append((n1, w))
#
# for _ in range(M):
#     s, e = map(int, input().split())
#     print(bfs(s, e))
#     print(link_arr)



