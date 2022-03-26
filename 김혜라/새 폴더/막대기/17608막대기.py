from sys import stdin

input = stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
# print(arr)
if n == 0:
    print(0)

if max(arr) == 0:
    print(0)
# try:
else:
    cnt = 1
    maxx = arr[-1]
    tallest = max(arr)
    # print(tallest)
    for i in range(n -1, -1, -1):
        # print(i)
        if arr[i] > maxx:
            cnt += 1

        if maxx < arr[i]:
            maxx = arr[i]

        if arr[i] == tallest:
            break
    print(cnt)

# except:
#     print(0)

