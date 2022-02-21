

a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + (a * 1000))

if a == b != c or a == c != b:
    print(1000 + (a * 100))


if b == c != a:
    print(1000 + (b * 100))

if a != b and b != c and a != c:
    maxx = max(a, b, c)

    print(maxx * 100)

