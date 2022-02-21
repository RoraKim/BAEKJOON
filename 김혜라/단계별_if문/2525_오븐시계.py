h, m = map(int, input().split())
time = int(input())

if m + time >= 60:
    h += (m + time) // 60
    m = m + time - ((m + time) // 60) * 60

elif m + time < 60:
    h = h
    m = m + time

if h > 23:
    h = h - 24

print(h, m)