n, m = map(int, input().split())

def choco(n, m):
    m = max(n, m)
    n = min(m, n)

    return (n - 1) + n * (m - 1)

print(choco(n, m))