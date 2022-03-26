# import sys;

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# maxx = 0
#
#
def dfs(start):
    visited[start] = True

    for i in arr[start]:
        if visited[i]:
            continue
        dfs(i)



# # dfs
# #visited를 정점 개수보다 하나 더 가진 걸로 생성
# #arr의 앞, 뒷값 모두 해당 인덱스에 연결된 노드를 적어줌
# # 조건에 맞는 애들은 다시 dfs로 (visited가아닌애들)
#

n, m = map(int, input().split())
arr = [[] * m for _ in range(n + 1)]
# print(arr)
visited = [0] * (n + 1)
cnt = 0
# print(visited)
for _ in range(m):
    u, v = map(int, input().split())
    # print(u)
    arr[u].append(v)
    arr[v].append(u)

# print(arr)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)

















# def dfs(cur):
#     visited[cur] = True
#
#     for nxt in arr[cur]:
#         if visited[nxt]:
#             continue
#
#         dfs(nxt)
#
#
# n, m = map(int, input().split())
# arr = [[] for i in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#
#     arr[a].append(b)
#     arr[b].append(a)
#
# visited = [False for i in range(n + 1)]
# print(arr)

#모든 요소가 연결되어 있다면 cnt의 값은 1이 나올 것이다
#정의한 dfs()실행 이후에 방문처리 되지 않은 요소가 있다는 것은
#별개의 연결요소가 존재한다는 뜻
#방문처리 후, cnt를 증가시켜준다.

# 우선 연결 요소란 서로 완전하게 이어져 있는 한 그래프 덩어리를 연결 요소라 한다.
# 만약 어떠한 경로라도 a to z로 갈 수 없다면 그것은 서로 한 모듈안에 있지 않다는 것이다.
# 입력으로 들어온 그래프의 연결 요소의 개수를 파악하려면 다음 순서로 찾아가면 풀 수 있다.

# 1. dfs 또는 bfs로 시작 노드부터 방문을 한다.

# 2. 한번 돈 후 check 배열에 아직 방문하지 못한 노드가 있다면
# 그것은 같은 모듈이 아니라는 뜻으로 그 노드부터 다시 탐색을 진행한다.

# 3. 1 ~ 2번을 모든 정점을 방문할 때 까지 진행한다.


# cnt = 0
# for i in range(1, n + 1):
#     print(i, visited)
#     if not visited[i]:
#         dfs(i)
#         cnt += 1
# # print(visited)
# print(cnt)
