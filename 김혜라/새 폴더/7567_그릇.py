arr = list(input())
# print(arr)

dish = 0
for i in range(len(arr) - 1):
    if i == 0:
        dish += 10

    if arr[i] == arr[i + 1]:
        dish += 5

    else:
        dish += 10

print(dish)