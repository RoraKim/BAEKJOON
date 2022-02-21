def safe(letter):
    n = len(letter)
    main_list = []
    for i in range(1, 1 << n):
        sub_list = []
        #j는 arr_a의 인덱스이므로 0부터 조회해야
        #모든 요소 포함 여부 확인 가능
        for j in range(n):
            if i & (1 << j):
                #print(arr[j], end=' ')
                sub_list.append(ord(letter[j]) - 64)
        main_list.append(sub_list)
    # #
    # print(main_list)

    # #길이 조건에 맞는 부분집합을 담은 함수 len_list
    len_list = []
    for i in main_list:
        if len(i) == 5:
            len_list.append(i)

    # len_list = sorted(len_list)
    return(len_list)



num, letter = map(str, input().split())
num = int(num)
# print(letter)
# print(ord('Z'))


alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



print(safe(letter))
print(len(safe(letter)))

# my_lst = []
# for i in safe(letter):
#     for j in i:
#         my_lst.append[j]
#


















#     sub_set = [[]]
#     for j in i:
#         len_ = len(sub_set)
#         for k in range(len_):
#             sub_set.append(sub_set[k] + [j])
#     # print(sub_set)
#
#     len_list = []
#     for i in sub_set:
#         if len(i) == 5:
#             len_list.append(i)
#
#     print(len_list)

    # main_list = []
    # for j in range(1, 1 << 5):
    #     sub_list = []
    #     #j는 arr_a의 인덱스이므로 0부터 조회해야
    #     #모든 요소 포함 여부 확인 가능
    #     for j in range(5):
    #         if i & (1 << j):
    #             #print(arr[j], end=' ')
    #             sub_list.append(letter[i][j])
    #     main_list.append(sub_list)
    # #
    # print(main_list)

    # #길이 조건에 맞는 부분집합을 담은 함수 len_list
    # len_list = []
    # for i in main_list:
    #     if len(i) == 5:
    #         len_list.append(i)
    #
    # print(len_list)

    # print(safe(i))
# for i in range(len((len_list))):
#     for j in range(i):

    # if (len_list[i][0]) - (len_list[i][1] ** 2) + (len_list[i][2] ** 3) - (len_list[i][3] **4) + (len_list[i][4] ** 5) == num:
    #     print(len_list)
