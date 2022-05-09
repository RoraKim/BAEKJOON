# s_sum : 선택된 것의 합계
# s_cnt : 선택된 것의 개수
# s : 목표하는 원소의 합
# n : 원소의 개수
# def dfs(level, s_cnt, s_sum):
#     # 가지치기
#     if s_cnt > n or s_sum > s:
#         return
#
#         # 종료조건
#     if level == n:
#         if s_sum == s:
#             global sol
#             # n개의 원소를 가지고 있고 원소 합이 k인 부분집합
#             sol += 1
#         return
#
#     dfs(level + 1, s_cnt + 1, s_sum + arr[level])
#     dfs(level + 1, s_cnt, s_sum)
#
#
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# sol = 0
# dfs(0, 0, 0)
# print(sol - 1)

import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def dfs(idx, s_sum):
    global cnt
    #인덱스가 원소 수를 넘어간 경우
    if idx >= n:
        return

    # 이번 탐색의 원소를 합해줌
    s_sum += arr[idx]
    if s_sum == s:
        cnt += 1

    #이번 탐색값을 포함해 다음 dfs
    dfs(idx + 1, s_sum)
    #이번 탐색값 제외 다음 dfs
    dfs(idx + 1, s_sum - arr[idx])

dfs(0, 0)
print(cnt)

# import sys
#
# input = sys.stdin.readline
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0
#
#
# def subset_sum(idx, sub_sum):
#     global cnt
#
#     if idx >= n:
#         return
#
#     sub_sum += arr[idx]
#
#     if sub_sum == s:
#         cnt += 1
#
#     # 현재 arr[idx]를 선택한 경우의 가지
#     subset_sum(idx + 1, sub_sum)
#
#     # 현재 arr[idx]를 선택하지 않은 경우의 가지
#     subset_sum(idx + 1, sub_sum - arr[idx])
#
#
# subset_sum(0, 0)
# print(cnt)












#
#
#
# def subset_sum(idx, sub_sum):
#     global cnt
#
#     if idx >= n:
#         return
#
#     sub_sum += arr[idx]
#
#     if sub_sum == s:
#         cnt += 1
#
#     # 현재 arr[idx]를 선택한 경우의 가지
#     subset_sum(idx + 1, sub_sum)
#
#     # 현재 arr[idx]를 선택하지 않은 경우의 가지
#     subset_sum(idx + 1, sub_sum - arr[idx])
#
#
# subset_sum(0, 0)
# print(cnt)

























# def dfs(L, beginwith):
#     global cnt
#     #종료 조건
#     if sum(result) == s:
#         cnt += 1
#         return cnt
#
#     #종료하지 않으면
#     else:
#         for i in range(beginwith, n):
#             result[L]=arr[i]
#             dfs(L+1, i+1)
#
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0
# result = [0] * n
# print(dfs(0,0))

