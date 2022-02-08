import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
if len(a) == n:
    for i in a:
        if i < x:
            result.append(i)

print(*result)

