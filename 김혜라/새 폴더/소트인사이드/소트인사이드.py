# import sys; sys.stdin = open('소트인사이드.txt')

import sys
input = sys.stdin.readline
score = input().rstrip()

arr = []
for i in score:
    arr.append(int(i))

arr.sort(reverse=True)

for i in arr:
    print(i, end='')
# print(arr)

