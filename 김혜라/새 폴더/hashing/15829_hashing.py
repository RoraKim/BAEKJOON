import sys; sys.stdin = open('15829_hashing.txt')

n = int(input())
arr = list(input())

# print(arr)
num = []
for i in arr:
    num.append(ord(i) - 96)

# print(num)

result = 0
for i in range(n):
    result += num[i] * (31 ** i)
    # print(result)

result = result % 1234567891
print(result)
