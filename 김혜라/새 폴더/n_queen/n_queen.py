
# def n_queen(i, col):
#     global cnt
#     if promising(i, col):
#
#         #promising한데 i가 n레벨까지 갔다면
#         if i == n:
#             # print(col[1::])
#             cnt += 1
#
#         #promising한데 n레벨까지 못갔다면
#         else:
#             for j in range(1, n+1):
#                 col[i + 1] = j
#                 n_queen(i+1, col)
#     return cnt
#
# def promising(i, col):
#     #확인할 열 번호
#     k = 1
#     flag = True
#     while k < i and flag:
#         if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
#             flag = False
#
#         k += 1
#     return flag
#
# n = int(input())
# col = [0] * (n + 1)
# cnt = 0
#
# print(n_queen(0, col))
# # #
# #
# #
# #
#
#
# import sys
# input = sys.stdin.readline
#
# def n_queen(i):
#     global cnt# i는 depth, col은 칼럼
#     #0부터 시작
#     #promising하다면
#
#     if i == n: #끝까지 다 왔다
#         #맨 앞 0 제외
#         # print(col)
#         cnt += 1
#
#     #promising하지만 끝까지 오지는 못했다
#     else:
#         #모든 j에 대해서
#         #(1,1)의 위치에 queen이 있다고 가정했을때, (2,1), (2,2) ... 확인
#         for j in range(n):
#             #(2,1), (2,2) ... 넣어주는 과정
#             col[i] = j
#
#             flag = True
#             # k가 i보다 작고 flag가 true인 동안에
#             for k in range(i):
#                 # 같은 열에 있는가, 또는 행의차와 열의차의 절댓값이 같은가
#                 if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
#                     # 이 조건에 걸리면  flag가 False가 되어 while을 벗어나기 때문에
#                     # return이 False가 됨
#                     flag = False
#                     break
#
#             if flag:
#                 n_queen(i + 1)
# #
# # def promising(i):
# #     flag = True
# #     #k가 i보다 작고 flag가 true인 동안에
# #     for k in range(i):
# #         #같은 열에 있는가, 또는 행의차와 열의차의 절댓값이 같은가
# #         if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
# #             #이 조건에 걸리면  flag가 False가 되어 while을 벗어나기 때문에
# #             #return이 False가 됨
# #             flag = False
# #             break
# #     return flag
# #
# n = int(input())
# col = [0]*n
# cnt = 0
# n_queen(0)
# print(cnt)
#==================================================================================
import sys
input = sys.stdin.readline

def n_queen(i):
    global cnt# i는 depth, col은 칼럼
    #0부터 시작
    #promising하다면

    if i == n: #끝까지 다 왔다
        #맨 앞 0 제외
        # print(col)
        cnt += 1

    #promising하지만 끝까지 오지는 못했다
    else:
        #모든 j에 대해서
        #(1,1)의 위치에 queen이 있다고 가정했을때, (2,1), (2,2) ... 확인
        for j in range(n):
            #(2,1), (2,2) ... 넣어주는 과정
            col[i] = j

            flag = True
            # k가 i보다 작고 flag가 true인 동안에
            for k in range(i):
                # 같은 열에 있는가, 또는 행의차와 열의차의 절댓값이 같은가
                if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
                    # 이 조건에 걸리면  flag가 False가 되어 while을 벗어나기 때문에
                    # return이 False가 됨
                    flag = False
                    break

            if flag:
                n_queen(i + 1)
#
# def promising(i):
#     flag = True
#     #k가 i보다 작고 flag가 true인 동안에
#     for k in range(i):
#         #같은 열에 있는가, 또는 행의차와 열의차의 절댓값이 같은가
#         if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
#             #이 조건에 걸리면  flag가 False가 되어 while을 벗어나기 때문에
#             #return이 False가 됨
#             flag = False
#             break
#     return flag
#
n = int(input())
col = [0]*n
cnt = 0
n_queen(0)
print(cnt)
#=====================================================================



# def promising(i):
#     for j in range(0, i):
#         # 새로운 퀸과 기존의 퀸이 같은 행에 있거나 대각선에 있을 경우
#         if row[j] == row[i] or abs(row[j] - row[i]) == (i - j):
#             return False
#     return True
# #
#
# def N_queen(i):
#     global result
#     if i == N:
#         result += 1
#     else:
#         for j in range(N):
#             row[i] = j
#             if promising(i):
#                 N_queen(i + 1)
#
#
# N = int(input())
# row = [0] * 15
# result = 0
# N_queen(0)
# print(result)