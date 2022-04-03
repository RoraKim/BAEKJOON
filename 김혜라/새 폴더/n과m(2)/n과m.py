# import sys; sys.stdin = open('n과m.txt')

# def dfs(l, beginwith):
#     global result
#     global result_arr
#     if l == m:
#         result_arr.append(result[:])
#
#     else:
#         for i in range(beginwith, n):
#                 result[l] = arr[i]
#                 dfs(l + 1, beginwith+1)


def dfs(L, beginwith):
    # 종료조건
    if L == m:
        # print(result)
        result_arr.append(result[:])

    else:
        for i in range(beginwith, n):
            result[L] = arr[i]
            dfs(L + 1, i + 1)


n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)
# print(arr)
visited = [0] * n
# print(visited)

result = [0] * m
result_arr = []
dfs(0, 0)
# print(result_arr)

for i in result_arr:

    print(*i)