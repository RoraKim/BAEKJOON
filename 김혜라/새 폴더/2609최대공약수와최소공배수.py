import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(min(n, m), 0, -1):
    if m % i == n % i == 0:
        print(i)
        break

for i in range(max(n, m), (n * m) + 1):
    if i % m == i % n == 0:
        print(i)
        break