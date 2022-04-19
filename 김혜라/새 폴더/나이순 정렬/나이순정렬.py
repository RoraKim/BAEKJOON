import sys; sys.stdin = open('나이순정렬.txt')

n = int(input())
arr=[]
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name, i+1))

# print(arr)

arr.sort(key=lambda x:(x[0], x[2]))
# print(arr)
for i in arr:
    print(i[0], end= ' ')
    print(i[1])
