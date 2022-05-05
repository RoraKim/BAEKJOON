import sys; sys.stdin = open('test.txt')

arr = [list(input()) for _ in range(5)]

print(arr)
#
# for i in range()
#

my_arr = [[-1] * 15 for _ in range(15)]
# print(my_arr)


for i in range(15):
    for j in range(15):
        try:
            # if arr[i][j] != -1:
                my_arr[i][j] = arr[i][j]

        except:
            pass

# print(my_arr)

for i in range(15):
    for j in range(15):
        if my_arr[j][i] != -1:
            print(my_arr[j][i], end='')
# for i in