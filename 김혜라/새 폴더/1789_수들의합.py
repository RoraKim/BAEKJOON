ans = int(input())

cnt = 0
result = 0
for i in range(1, ans+1):
    if ans < result:
        print(cnt - 1)
        break

    else:
        result += i
        cnt += 1

s = int(input())
N = 0
result = 0
for i in range(1, s + 1):
    result += i
    N += 1

    if (result > s):
        N -= 1
        break

print(N)


