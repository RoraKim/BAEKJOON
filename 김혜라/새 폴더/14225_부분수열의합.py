import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
result = [-1] * 10000000
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        summ = sum(x)
        result[summ] += 1

for i in range(1, len(result)):
    if result[i] == -1:
        print(i)
        break



