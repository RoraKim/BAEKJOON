x_arr = []
y_arr = []
for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

x_arr.sort()
y_arr.sort()

first_x = x_arr[0]
last_x = x_arr[-1]

if x_arr.count(first_x) == 2:
    print(last_x, end=' ')

else:
    print(first_x, end=' ')

# print(x_arr.count(first_x))
# print(y_arr)

first_y = y_arr[0]
last_y = y_arr[-1]

if y_arr.count(first_y) == 2:
    print(last_y, end=' ')

else:
    print(first_y, end=' ')


