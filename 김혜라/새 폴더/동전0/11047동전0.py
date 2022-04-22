import sys; sys.stdin = open('11047동전0.txt')

n , k = map(int, input().split())
arr = []
for i in range(n):
    coin = int(input())
    arr.append(coin)


count = 0
for i in range(n - 1, -1, -1):
    count += k//arr[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    k = k % arr[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)















# print(arr)
# result = 0
# for i in range(n - 1, -1, -1):
#     print(arr[i])
#     j = 1
#     summ = 0
#     while True:
#         summ = summ + arr[i] * j
#         if summ >= k:
#             j -= 1
#             result += j
#             break
# print(result)


