n = int(input())
my_list = list(map(int, input().split()))
# print(my_list)
sorted_list = []
for i in range(n-1,0,-1):
    for j in range(0, i):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

m = my_list[-1]
new_sum = 0
for i in range(n):
    new_sum += my_list[i] / m * 100
    
print(new_sum / n)


