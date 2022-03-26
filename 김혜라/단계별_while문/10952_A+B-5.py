from sys import stdin
for line in stdin:
    a, b = map(int, line.split())
    print(a + b)


# import sys; sys.stdin = open('10942.txt')
#
# while True:
#
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a + b)

