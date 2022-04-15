import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
n, m = map(int, input().split())
#
# queue = []
# for i in range(n, m+1):
#     queue.append(i)
#
# print(queue)
#
# for i in queue:
#     cnt = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             cnt += 1
#
#         if cnt >= 3:
#             break
#
#     if cnt == 2:
#         queue.pop()

# def prime_list(n, m):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * (m - n + 1)
#
#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#     x = int(m ** 0.5)
#     for i in range(n, x + 1):
#         if sieve[i] == True:           # i가 소수인 경우
#             for j in range(i+i, m - n + 1, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False
#
#     # 소수 목록 산출
#     return [i for i in range(0, m -n + 1) if sieve[i] == True]
#
#
#
#
# print(prime_list(n, m))




# for i in range(n, m+1):
#     cnt = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             cnt += 1
#
#         if cnt >= 3:
#             break
#
#     if cnt == 2:
#         print(i)


def check_prime(num):
    if num == 1:
        return False

    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


for i in range(n, m + 1):
    if check_prime(i):
        print(i)


#하민스 코드
# M, N = map(int, input().split())
#
# prime_list = [0] * (N+1)
# prime_list[0] = 1
# prime_list[1] = 1
# result = []
# for i in range(2, N+1):
#     if prime_list[i] == 0:
#         if i >= M:
#             result.append(i)
#         for j in range(i, N+1, i):
#             prime_list[j] = 1
# for k in result:
#     print(k)