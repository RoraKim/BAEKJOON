
words = input()
upper_words = words.upper()
# print(upper_words)
set_words = list(set(upper_words))
# print(set_words)

cnt_dic = dict()
cnt_arr = []
for i in set_words:
    cnt_dic[i] = upper_words.count(i)
    cnt_arr.append(upper_words.count(i))
    maxx = max(cnt_arr)

# print(cnt_dic)
cnt = 0
for key, item in cnt_dic.items():
    if item == maxx:
        cnt += 1
        maxx_letter = key

if cnt == 1:
    print(maxx_letter)

else:
    print('?')




    # cnt_arr.append(upper_words.count(i))
# print(cnt_arr)
















# max_letter = ''
# cnt_arr = []
# maxx_cnt = 0
# a = 0
# for i in set_words:
#     cnt = upper_words.count(i)
#     # retunn = (i, cnt)
#     #
#     # cnt_arr.append(retunn)
#     # print(cnt_arr)
#     if cnt > maxx_cnt:
#         maxx_cnt = cnt
#         max_letter = i
#         cnt = 0
#     if maxx_cnt == cnt:
#         a = '?'
#         print(a)
#         break
#
# if a != '?':
#     print(max_letter)


