

n = input()
if int(n)<10:
    n = '0' + n

origin_n = n
new_num = -1
cnt = 0
while origin_n != new_num:
    summ = int(n[0]) + int(n[1])
    right_summ = str(summ)[-1]
    # print(n[0])
    new_num = n[1] + str(summ)[-1]
    n = new_num
    cnt += 1
    # print(right_summ)
    # print(new_num)
print(cnt)












# N = input()
#
# new_num = N
# count = 0
# if int(new_num) < 10:
#     front = '0' + N
#     back = N
#     new_num = front[-1] + back[-1]
#     new_num = int(new_num[0]) + int(new_num[1])
#     count += 1
#
# while new_num != int(N):
#
#     front = str(new_num)[-1]
#     if int(new_num) >= 10:
#         back = str(int(str(new_num)[0]) + int(str(new_num)[1]))
#     else:
#         back = str(int(str(new_num)[0]))
#     if back == N:
#         print(count)
#         break
#     count += 1
#     new_num = int(front + back[-1])
#
#
# print(count)
#
