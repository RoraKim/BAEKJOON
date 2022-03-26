arr = []
for t in range(10):
    a = int(input())
    left = a % 42
    arr.append(left)
    sett = set(arr)

print(len(sett))
