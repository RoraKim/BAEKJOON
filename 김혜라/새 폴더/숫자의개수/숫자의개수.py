a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result = str(result)
# print(result)

for i in range(10):
    print(result.count(str(i)))