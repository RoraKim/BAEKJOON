import sys
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    for j in range(i + 1):
        a = '*' * (j + 1)

    print(a.rjust(N))