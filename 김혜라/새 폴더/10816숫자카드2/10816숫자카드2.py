import sys; sys.stdin = open('10816숫자카드2.txt')

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
search = list(map(int, input().split()))

big_arr = [0 for _ in range(20000002)]

for i in arr:
    if i < 0:
        big_arr[-i] += 1
    elif i > 0:
        big_arr[10000001 + i] += 1

    else:
        big_arr[10000001] += 1

for j in search:
    if j < 0:
        j = -j
    elif j > 0:
        j = 10000001 + j

    elif j == 0:
        j = 10000001

    print(big_arr[j], end=' ')











# print(arr)
# print(search)
#
# for i in search:
#     print(arr.count(i), end=' ')
