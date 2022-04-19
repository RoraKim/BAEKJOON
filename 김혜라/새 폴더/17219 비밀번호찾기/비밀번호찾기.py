import sys; sys.stdin = open('비밀번호찾기.txt')
# input = sys.stdin.readline

n, m = map(int, input().split())

arr = dict()
for i in range(n):
    site, password = input().split()
    arr[site]=password

# print(arr)
    # print(arr)
for j in range(m):
    site = input()
    print(arr.get(site))



