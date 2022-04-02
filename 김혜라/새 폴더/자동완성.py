# word = input()
#
# if word == 'N' or word == 'n':
#     print('Naver D2')
#
# else:
#     print("Naver Whale")


word = input()

k = ''
for i in word:
    if i == '/':
        break
    k+= i
new_word = word.replace(k + '/', '')
# print(b)
k = int(k)
# print(k)

d = ''
for i in new_word:
    if i == '/':
        break
    d+= i
new_word = new_word.replace(d + '/', '')

d = int(d)
a = int(new_word)

# print(k)
# print(d)
# print(a)

if k + a < d or d == 0:
    print('hasu')

else:
    print('gosu')

