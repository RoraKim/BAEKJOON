k, n, m = map(int, input().split())

need = k * n
have = m

if need > have:
    print(need - have)
else:
    print(0)