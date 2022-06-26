
# a, b = input().split()
# a = ord(a)
# b = ord(b)
#
# if a < b:
#     for i in range(a, b+1):
#         print(chr(i), end=' ')
#
# else:
#     for i in range(a, b-1, -1):
#         print(chr(i), end=' ')

# def fun(a):
#     if a == 0:
#         return
#     print(a * '*')
#     fun(a - 1)
#     print(a * '*')
#
# fun(int(input()))










# import sys
# N = int(sys.stdin.readline().rstrip())
# #
# for i in range(N -1, -1, -1):
#     for j in range(i + 1):
#         a = '*' * (j + 1)
#
#     print(a.rjust(N))

# n = list(input())
#
#
# for i in range(len(n)):
#
#
#     if i == len(n) - 1:
#         print(n[i])
#
#     else:
#         print(n[i], end=',')

#
# for i in range(n):
#     for j in range(n):

# n = list(input())
# n = reversed(n)
#
# for i in n:
#     print(i, end='')
# print(n)

# arr = [1, 3, 5, 7, 9]
#
# n = int(input())
# a = 0
# for i in range(n):
#     for j in range(n):
#         print(arr[(i + j + a) % 5], end=' ')
#     a += 2
#     print()

# a = input()
#
# for i in range(len(a)):
#     a = a[-1] + a[:len(a)-1]
#     print(a)
#
# lst = []
# a = input()
# lst.append(a)
# b = input()
# lst.append(b)
# c = input()
# lst.append(c)
#
# sorted_lst = sorted(lst)
#
# # print(sorted_lst)
# # print(lst)
#
# if sorted_lst == lst:
#     print('YES')
#
# else:
#     print('NO')





# lst = list(input().split())
# lst.sort()
# print(lst[0])
#
# a = 'Pennsylvania'
# n = input()
#
# for i in range(0,len(a)-len(n)):
#     if a[i] !=

# def bruteforce(pattern, text):
#     #     pattern : 찾고자하는 문자열
#     #     text : 비교대상 문자열
#     i = 0 #text의 검색 인덱스
#     j = 0 #pattern의 검색 인덱스
#     while i < len(text) and j < len(pattern):
#         if text[i] != pattern[j]:
#             i = i - j
#             j = -1
#         i += 1
#         j += 1
#
#     if j == len(pattern):
#         return True
#
#     else:
#         False
#
# pattern = input()
# text = 'Pennsylvania'
# print(bruteforce(pattern, text))

#
# text = list(input().split())
# spliter = input()
#
# # print(text)
#
# for i in range(len(text)):
#     if text[i] == spliter:
#         print()
#     else:
#         print(text[i], end=' ')




# a = input().split(' (space) ')
# a.reverse()
# # print(a)
# for i in a:
#     i.lstrip()
#     print(i)

# text, x, y = input().split()
#
# x, y = int(x), int(y)
#
# for i in range(y):
#     text = text[x:len(text)] + text[0:x]
#     print(text)


# lst = list(input().split())
#
# lst.sort()
# print(lst[0])
# # print(lst[-1])
#
# a, b, n = input().split()
# n = int(n)
# a = a + b
# print(a)
# b = a[0:n] + b[n:len(b)]
# print(b)




#
# while(True):
#     a = input()
#     if a == 'END':
#         break
#
#     print(a[::-1])

    # a = list(a)
    # a.reverse()
    # b = ''.join(a)

    # print(b)

# a = input()
#
# if a.isupper():
#     print('U')
#     print(a.upper())
#
# elif a.islower():
#     print('L')
#     print(a.upper())
#
# else:
#     print('X')
#     print(a.upper())


# a = int(input())
#
# lst = []
# for i in range(1, a + 1):
#     lst.append(i**2)
#
# print(lst)

# a = list(input().split())
# a.sort()
#
# dic = dict()
# for i in a:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
#
# # print(dic)
# dic = sorted(dic.items())
# # print(dic)
#
# for i in dic:
#     print(f'{i[0]} : {i[1]}')

#
# arr = list(map(int, input().split()))
#
# # print(arr)
#
# dic = dict()
#
# for i in arr:
#     if i//10 in dic:
#         dic[i//10] += 1
#
#     else:
#         dic[i//10] = 1
#
# # print(dic)
#
# lst = sorted(dic.items())
# # print(lst)
#
# for i, j in lst:
#     print(f'{i} : {j}')



#
# arr = [100]
# n = int(input())
# origin_n = n
# arr.append(origin_n)
#
# while arr[-2] - n >=0:
#     if n == origin_n:
#         n = arr[0] - n
#     else:
#         arr.append(n)
#         n = arr[-2] - n
#
# print(*arr)
# #
#
# first_arr = [5, 8, 10, 6, 4]
# second_arr = [11, 20, 1, 13, 2]
# third_arr = [7, 9, 14, 22, 3]
#
# for i in first_arr:
#     if i >= 10:
#         print(f'{i}', end='   ')
#
#     else:
#         print(f' {i}', end='   ')
# print()
#
# for i in second_arr:
#     if i >= 10:
#         print(i, end='   ')
#
#     else:
#         print(f' {i}', end='   ')
# print()
#
# for i in third_arr:
#     if i >= 10:
#         print(i, end='   ')
#
#     else:
#         print(f' {i}', end='   ')
# print()



# first_array = [list(map(int, input('first array').split()))] + [list(map(int, input().split()))]
# second_array = [list(map(int, input('second array').split()))] + [list(map(int, input().split()))]

# print(first_array)
# print(second_array)
# final = first_array * second_array
# print(final)

# for i in range(2):
#     for j in range(4):
#         print(first_array[i][j] * second_array[i][j], end=' ')
#
#     print()




# def check(arr):
#     if sum(arr) // 4 >= 80:
#         print('pass')
#         return 'pass'
#
#     else:
#         print('fail')
#         return 'fail'
#
#
# cnt = 0
# for i in range(5):
#     a = check(list(map(int, input().split())))
#     a
#     if a == 'pass':
#         cnt += 1
#
# print(f'Successful : {cnt}')
#
# arr = [[1] * 5 for _ in range(5)]
#
# for i in range(1, 5):
#     for j in range(1, 5):
#         arr[i][j] = arr[i-1][j] + arr[i][j-1]
#
# # print(arr)
#
# for i in arr:
#     print(*i)





# n = int(input())
#
# arr = []
# for i in range(n):
#     a = 'No.' + str(i + 1)
#     arr.append(a)
#
# print(arr)



#
#
# a, b = map(int, input().split())
# arr = [True for _ in range(a)]
# # print(a)
# # print(arr)
#
# for i in range(a):
#     if i % b == 0:
#         pass
#     else:
#         arr[i] = False
#
# print(arr)




# arr = list(map(int, input().split()))
#
# result = [[i, 0] for i in range(1, 7)]

# print(result)


# for i in arr:
#     for j in range(len(result)):
#         if i == j+1:
#             result[j][1] += 1
#
# # print(result)
#
# for i in result:
#     print(f'{i[0]} : {i[1]}')










#
# a = input()
#
# # print(a)
#
# b, c = input().split()
# # print(b)
# # print(c)
# print(a.count(b))
# print(a.replace(b,c))

# arr = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]
#
# a, b = map(int, input().split())
#
# print(arr[a-1] + arr[b-1])

# lst = []
# for i in range(5):
#     a = input()
#     lst.append(a)
#
# for i in range(4, -1, -1):
#     print(lst[i])



# arr = [input() for _ in range(10)]
# # print(arr)
# chr = input()
# #
# # print(arr)
#
#
#
#
#
# for i in arr:
#     if i[-1] == chr:
#         print(i)
#
# arr = list(map(int, input().split()))
# min_arr = []
# max_arr = []
# for i in arr:
#     if i <100:
#         min_arr.append(i)
#
#     else:
#         max_arr.append(i)
#
# try:
#     print(max(min_arr), end=' ')
#
# except:
#     print(100, end=' ')
#
# try:
#     print(min(max_arr), end=' ')
#
# except:
#     print(100, end=' ')






#
# arr = list(map(int, input().split()))
# summ = 0
# avg = 0
# for i in range(10):
#     if i%2:
#         summ += arr[i]
#
#     else:
#         avg += arr[i]
#
# print(f'sum : {summ}')
# print(f'avg : {avg / 5:0.1f}')








# arr = map(int, input().split())
# b = sorted(arr, reverse=True)
# print(*b)


# arr = [input() for _ in range(5)]
# # print(arr)
# b = sorted(arr, reverse=True)
# # print(b)
# for i in b: print(i)

# arr = []
# while True:
#     a = int(input())
#     if a == -1:
#         break
#
#     arr.append(a)
#
# if len(arr) <3:
#     print(*arr)
#
# else:
#     print(*arr[-3::])


#
#
# arr = list(map(float, input().split()))
# print(arr)
#
# print(f'{sum(arr) / 6:0.1f}')

# arr = list(map(int, input().split()))
#
# print(f'max : {max(arr)}')
# print(f'min : {min(arr)}')


# arr = list(map(int, input().split()))
# cnt = 0
# summ = 0
#
# for i in arr:
#     if i % 5 == 0:
#         cnt += 1
#         summ += i
#
# print(f'Multiples of 5 : {cnt}')
# print(f'sum : {summ}')
# print(f'avg : {summ / cnt:0.1f}')


# arr = list(map(int, input().split()))
# print(len(arr))
#
# for i in arr:
#     if i % 2 == 0:
#         print(i // 2, end=' ')
#
#     else:
#         print(i * 2, end=' ')


# n = int(input())
#
# arr = list(map(int, input().split()))
#
# b = sorted(arr, reverse=True)
#
# for i in range(n):
#     print(b[i])


# arr = ["flower", "rose", "lily", "daffodil", "azalea"]
#
# a = input()
# cnt = 0
# result = []
# for i in arr:
#     if i[1] == a or i[2] == a:
#         result.append(i)
#         cnt += 1
#
#
# if len(result) == 0:
#     print(0)
#
# else:
#     for i in result:
#         print(i)
#
#     print(cnt)



# arr = []
# while True:
#     a = input()
#     if a == '0':
#         break
#
#     arr.append(a)
#
# print(len(arr))
#
# for i in arr:
#     if 'mo' in i:
#         print(i)

#
#
#
#
#
# arr = [input() for _ in range(5)]
#
# a = input()
# b = input()
#
#
#
#
#
# result = []
# for i in arr:
#     if a in i or b in i:
#         result.append(i)
#
# if len(result) == 0:
#     print('none')
#
# else:
#     for i in result:
#         print(i)














# /

# print(ord('A'))

























#
# row, column = 1, int(input())
#
# for i in range(1, column + 1):
#     for j in range(1, column + 1):
#         print((i, j), end=' ')
#     print()


# print(ord('A'))
# # print(ord('Z'))
#
# for i in range(65, 91):
#     print(chr(i),end='')















# a, b = map(int, input().split())
#
# if a < b:
#     for i in range(1, 10):
#         for j in range(a, b+1):
#             if i * j >= 10:
#                 print(f'{j} * {i} = {i * j}', end='   ')
#             else:
#                 print(f'{j} * {i} =  {i * j}', end='   ')
#         print()
#
#
# else:
#     for i in range(1, 10):
#         for j in range(a, b - 1, -1):
#             if i * j >= 10:
#                 print(f'{j} * {i} = {i * j}',end='   ')
#             else:
#                 print(f'{j} * {i} =  {i * j}',end='   ')
#         print()

# a, b = map(int,input().split())
#
# minn = min(a, b)
# maxx = max(a, b)
#
# cnt = 0
# summ = 0
#
# for i in range(minn,maxx + 1):
#     if i % 3 == 0:
#         summ += i
#         cnt += 1
#
#     elif i % 5 == 0:
#         summ += i
#         cnt += 1
#
# print(f'sum : {summ}')
# print(f'avg : {summ / cnt:0.1f}')



# a = int(input())
#
# for i in range(1, 11):
#     print(a * i, end=' ')








# a = int(input())
#
# summ = 0
# for i in range(0, a + 1, 5):
#     summ += i
#
# print(summ)
#
# arr = list(map(int, input().split()))
#
# odds = 0
# evens = 0
# for i in arr:
#     if i % 2:
#         odds += 1
#     else:
#         evens += 1
#
# print(f'even : {evens}')
# print(f'odd : {odds}')




#
# print(f'{sum(arr)/len(arr):0.2f}')






















# a = input()
# print(a * 20)

# for i in range(10, 21):
#     print(i, end=' ')

# a = int(input())
# for i in range(2, a + 1, 2):
#     print(i, end=' ')

# a = int(input())
# summ = 0
# for i in range(a, 100+1):
#     summ += i
#
# print(summ)



# arr = list(map(int, input().split()))
# # print(arr)
#
# three = 0
# five = 0
# for i in arr:
#     if i % 3 == 0:
#         three += 1
#
#     if i % 5 == 0:
#         five += 1
#
# print(f'Multiples of 3 : {three}')
# print(f'Multiples of 5 : {five}')

# arr = list(map(int, input().split()))
#
# avg = sum(arr) / len(arr)
# print(f'avg : {avg:0.1f}')
# if avg >= 80:
#     print('pass')
# else:
#     print('fail')

#
# for i in range(2, 7):
#     print(i, end=' ')
# print()
# for i in range(3, 8):
#     print(i, end=' ')
# print()
# for i in range(4, )


# /

# for i in range(2, 5):
#     for j in range(1, 6):
#         if i * j >= 10:
#             print(f'{i} * {j} = {i * j}', end='   ')
#         else:
#             print(f'{i} * {j} =  {i * j}', end='   ')
#     print()

# a, b = map(int, input().split())
# # print(a, b)
# minn = min(a, b)
# maxx = max(a, b)
# # print(a, b)
#
# for i in range(minn, maxx + 1):
#     print(i, end=' ')

# for i in range(a):
#     print('JUNGOL')




































# for i in range(1, 16):
#     print(i, end=' ')
#
# a = int(input())
# ans = 0
# while a >= 1:
#     ans = a + ans
#     a -= 1
#
# print(ans)

# a = 'a'
#
# while True:
#     print('1. Korea	\n2. USA \n3. Japan \n4. China')
#     a = int(input("number? "))
#
#     if a == 1:
#         print("Seoul")
#
#     elif a == 2:
#         print("Washington")
#
#     elif a == 3:
#         print("Tokyo")
#
#     elif a == 4:
#         print("Beijing")
#
#     else:
#         print("none")
#         break

# a = 2
# cnt = 0
# while a != 0:
#     a = int(input())
#     if a % 3 != 0 and a % 5 != 0:
#         cnt += 1
#
# # print(cnt)
#
# while True:
#     a = int(input("Width = "))
#     b = int(input("Height = "))
#     print(f'Triangle Area = {a * b / 2:0.1f}')
#     con = input("Continue? ")
#     if con == 'Y' or con =="y":
#         pass
#
#     else:
#         break












# a = float(input())
#
# if a >= 4.0:
#     print("scholarship")
#
# elif a >= 3.0:
#     print("next semester")
#
# elif a >= 2.0:
#     print("seasonal semester")
#
# else:
#     print("retake")

# a, b, c = map(int, input().split())
#
# print(a) if a == min(a, b, c) else print(b) if b == min(a, b, c) else print(c)

# a = int(input())
#
# if a % 400 == 0:
#     print("leap year")
#
# elif a % 4 == 0 and a % 100 != 0:
#     print("leap year")
#
# else:
#     print("common year")

# a = int(input())
#
# if a == 1:
#     print(31)
#
# elif a == 2:
#     print(28)
#
# elif a == 3:
#     print(31)
#
# elif a == 4:
#     print(30)
#
# elif a == 5:
#     print(31)
#
# elif a == 6:
#     print(30)
#
# elif a == 7:
#     print(31)
#
# elif a == 8:
#     print(31)
#
# elif a == 9:
#     print(30)
#
# elif a == 10:
#     print(31)
#
# elif a == 11:
#     print(30)
#
# else:
#     print(31)


















# print('5 Dan')
# print('5 * 2 = 10')
#
# print('6 + 2 = 8')
# print('6 - 2 = 4')
# print('My hometown')
# print('TTTTTTTTTT')
# print('TTTTTTTTTT')
# print('    TT')
# print('    TT')
# print('    TT')

# a = 49
# b = 0.2683
# # c = 2008
# # d = 1999
#
# print(a,'*',b, '=', a*b)
# print(c,'-',d, '=', c-d)

# a, *b = input().split()
# # print(*b)
#
# print('Your school is', *b, end='')
# print('.')

# string = int(input('Number 1? '))
# string2 = int(input('Number 2? '))
# print(string, '*', string2, '=', string * string2)
# print(string, '/', string2, '=', string / string2)

# garo = list(input().split())
# sero = list(input().split())
#
# a = float(garo[-1])
# b = float(sero[-1])

# garo = input()
# garo = float(garo.lstrip('Garo : '))
# # print(garo)
#
# sero = input()
# sero = float(sero.lstrip('Sero : '))
# # print(sero)
# # print(a * b)
# print(garo * sero)
#
# a = float(input('Garo : '))
# b = float(input('Sero : '))
#
# print(a * b)

# a = int(input())
# b = int(input())
# c = int(input())
#
# print('sum :', a + b + c)
# print('avg :', (a + b + c) // 3)
# print(a, '*', b, '=', a * b)

# a = float(input('yard? '))
# print(a, 'yard =', 91.44 * a, 'cm')
#

# 무하고있나 싶져? 정올 풀고이씁니다..
#
# a = int(input('Brother? '))
# b = int(input('Sister? '))
#
# print(True if a != b else False)
# c = int(input())
# d = int(input())

# print('width =', a)
# print(f'width = {a}')
# print('length =', b)
# print('area =', a *b)

# c_name, c_age = input().split()
# m_name, m_age = input().split()
# # c = int(input())
#
# print(c_name,'age', '+', m_name, 'age', "=", int(c_age) + int(m_age))
# print(a + '&' + b)

# name = input()
# age = input()
# score = input()
#
# print(f'I am {name}(IdNo. {age}). I got {float(score):.6f} in my midterm exam.')

# a = input().rstrip()
# b = input().rstrip()

# print(a, b)
#
# print(f'{"item":>10s}', end='')
# print(f'{"count":>10s}', end='')
# print(f'{"price":>10s}', end='')
# print(f'{"rate":>10s}')
# print(f'{"pen":>10s}', end='')
# print(f'{"20":>10s}', end='')
# print(f'{"100":>10s}', end='')
# print(f'{"50.5":>10s}')
# print(f'{"note":>10s}', end='')
# print(f'{"5":>10s}', end='')
# print(f'{"95":>10s}', end='')
# print(f'{"35.3":>10s}')
# print(f'{"eraser":>10s}', end='')
# print(f'{"110":>10s}', end='')
# print(f'{"97":>10s}', end='')
# print(f'{"14.2":>10s}')




# a, b, c = map(int, input().split())
# print(((a + b) * c) / 2)

# a = float(input('lb? '))
#
# print(f'{a:.1f}lb is {a * 0.45 :.1f}kg.')


# print(['Salad', 'Pizza', 'Chicken', 'Soup'])

# a = ['Python', 'is', 'exciting']
#
# print(*a)

# a = input()
# print(a[0])
# a = list(a)
# print(a[2])

# lst_odd = []
# lst_even = []
# a = input('Element? ')
# lst_odd.append(a)
#
# b = input('Element? ')
# lst_even.append(b)
#
# c = input('Element? ')
# lst_odd.append(c)
#
# d = input('Element? ')
# lst_even.append(d)
#
# e = input('Element? ')
# lst_odd.append(e)
#
# f = input('Element? ')
# lst_even.append(f)
# # index = int(input('Index? '))
#
# print(lst_odd + lst_even)

# lst = []
# for i in range(1, 16):
#     lst.append(i)
#
# # print(lst)
#
# a = int(input())
#
# result = []
# for i in lst:
#     if i % a == 0:
#         result.append(i)
#
# print(result)

# lst = list(input().split())
# print(lst[::-1])
#
# a = list(input())
# print(a[::-1])
#
#
# a = float(input())
# b = float(input())
#
# if a >= 4.0 and b >= 4.0:
#     print('A')
#
# elif a >= 3.0 and b >= 3.0:
#     print("B")
#
# else:
#     print('C')
#





# print(a, '>', b, '---', a > b)
# print(a, '<', b, '---', a < b)
# print(a, '>=', b, '---', a >= b)
# print(a, '<=', b, '---', a <= b)



# print(a + ' > ' + b + ' --- ' + 'True' if int(a) > int(b) else a + ' > ' + b + ' --- ' + 'False')
# print(a + ' < ' + b + ' --- ' + 'True' if int(a) < int(b) else a + ' < ' + b + ' --- ' + 'False')
# print(a + ' >= ' + b + ' --- ' + 'True' if int(a) >= int(b) else a + ' >= ' + b + ' --- ' + 'False')
# print(a + ' <= ' + b + ' --- ' + 'True' if int(a) <= int(b) else a + ' <= ' + b + ' --- ' + 'False')

# print(a + ' > ' + b + ' --- ' + 'False')
# print(a + ' < ' + b + ' --- ' + 'True')
# print(a + ' >= ' + b + ' --- ' + 'False')
# print(a + ' <= ' + b + ' --- ' + 'True')

# print(True) if a == b else print(False)
#
# print(False if a == b else True)
# if a == b: print(False),print(True)




# tup = ('Forest', 'Ocean', 'Mountain', 'Plain')
#
# a = int(input())
#
# if a in (1, 2, 3, 4):
#     print(tup[a - 1])
#
# else:
#     print('Input Error')



#
# a = ('Dolphin','Oh My Girl')
# b = ('Pallette','IU')
# c = ('Yes or Yes', 'Twice')
#
# print('[Song by Artist]')
# print('==========')
# print(*a)
# print(*b)
# print(*c)
#
# arr = list(map(float, input().split()))
#
# print(f'{(arr[0] + arr[-1]) / 2:0.1f}')



# n = int(input())
#
# for i in range(n+2, -1, -2):
#     print(('*' * i).center(n+2))



# n = int(input())
#
# def recursive(n):
#     if n == 0:
#         return
#
#     print('recursive')
#     recursive(n - 1)
#
# recursive(n)


#
# n = int(input())
#
# def recursive(n, summ):
#     summ += n
#     # print(summ)
#
#     if n == 0:
#         return summ
#
#     return recursive(n-1, summ)
#
#
#
#
# print(recursive(n, 0))



# from itertools import product
#
# n = int(input())
# arr = [i + 1 for i in range(6)]
# # print(arr)
# result = list(product(arr, repeat=n))
# # print(result)
# #
# for i in result:
#     print(*i)

# from itertools import permutations
#
# n = int(input())
# arr = [i + 1 for i in range(6)]
# print(arr)
# result = list(permutations(arr, n))
# print(result)

# for i in result:
#     print(*i)





#
# for i in range(int(input())):
#     print("~!@#$^&*()_+|")

# n = int(input())
#
# circle = 3.14 * n * n
#
# print(f'{circle:0.2f}')



# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print(i * n + j + 1, end=' ')
#     print()


# def fuc(a, b, c):
#     return (max(a, b, c))
#
#
# a, b, c = map(int, input().split())
#
# print(fuc(a, b, c))

# import sys
# sys.setrecursionlimit(5000)
#
# m, n = map(int, input().split())
# x = m
# def fuc(m, n):
#     global x
#     if n == 1:
#         return m
#
#     m = m * x
#     n = n - 1
#     # print(m, n)
#     return fuc(m, n)
#
# print(fuc(m, n))



# m, n = map(int, input().split())
#
# def fuc(m, n):
#     return m ** n
# print(fuc(m, n))

# a, b, c = input().split()
#
# a = int(a)
# c = int(c)
#
# if b == '+':
#     print(f'{a} + {c} = {a + c}')
#
# elif b == '*':
#     print(f'{a} * {c} = {a * c}')
#
# elif b == '/':
#     print(f'{a} / {c} = {a // c}')
#
# elif b == '-':
#     print(f'{a} - {c} = {a - c}')
#
# else:
#     print(0)












#
#
#
# a, b = map(int, input().split())
#
#
# def fuc():
#     global a, b
#     if a > b:
#         a = a // 2
#         b = b * 2
#         print(a, b)
#
#     else:
#         b = b // 2
#         a = a * 2
#         print(a, b)
#
#
# fuc()
#
#
#
#
#


# a, b = map(int, input().split())
#
# if a > b:
#     a, b = b, a
#
# for i in range(a, b + 1):
#     print(f'== {i}dan ==')
#     for j in range(1, 10):
#         result = i * j
#         print(f'{i} * {j} = {str(result).rjust(2)}')
#
#     print()

# def fuc(n):
#     if n == 4:
#         return
#     if n == 1:
#         print('first')
#
#     elif n == 2:
#         print('second')
#
#     elif n == 3:
#         print('third')
#
#     print('@@@@@@@@@@')
#     fuc(n + 1)
#
# fuc(1)


# n = int(input())
# m = 0
# def fuc(n):
#     global m
#     if n == 0:
#         return m
#
#     m += n
#     return fuc(n - 1)
#
# print(fuc(n))





# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=' ')
#
#     print()

#
# a, b = map(int, input().split())
#
# if a < b:
#     a, b = b, a
#
#
# def fuc(a, b):
#     print(a ** 2 - b ** 2)
#
# fuc(a, b)





# a, b, c = map(int, input().split())
# d, e, f = map(int, input().split())
# g, h, i = map(int, input().split())
#
# print(a, b, c, a + b + c)
# print(d, e, f, d + e + f)
# print(g, h, i, g + h + i)
# print(a + d + g, b + e + h, c + f + i, a + b + c + d + e + f + g + h + i)


#
# n = int(input())
#
# arr = list(map(int, input().split()))
#
# b = sorted(arr, reverse = True)
# print(*b)
#
# a, b = map(int, input().split())
# if abs(a) > abs(b):
#     print(a)
#
# else:
#     print(b)
#
# c, d = map(float, input().split())
# if abs(c) < abs(d):
#     print(c)
#
# else:
#     print(d)
#
# a = int(input())
#
# result = (a / 3.14) ** (1 / 2)
#
# print(f'{result:0.2f}')

# import math
#
# arr = list(map(float, input().split()))
# a = max(arr)
# b = min(arr)
# print(math.ceil(max(arr)), end=' ')
# print(math.floor(min(arr)), end=' ')
#
# arr.remove(a)
# arr.remove(b)
# # print(arr)
# print(round(arr[0]))








#
# arr = list(map(int, input().split()))
#
# def bubble_sort(arr):
#     for i in range(len(arr) - 1, 0, -1):
#         for j in range(i):
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#         print(*arr)
#
#
#
# bubble_sort(arr)





# n = int(input())
# arr = list(map(int, input().split()))
#
# def bubble(arr):
#     for i in range(n-1, 0, -1):
#         for j in range(i):
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#     return arr
#
# print(*bubble(arr))

# import math
#
# a, b = map(float, input().split())
# if a > b:
#     a, b = b, a
# # print(math.sqrt(a), math.sqrt(b))
# a = math.ceil(math.sqrt(a))
# b = math.floor(math.sqrt(b))
#
# # print(a, b)
#
# print(b - a + 1)








# arr = list(map(int, input().split()))
# summ = 0
# for i in arr:
#     if i < 0:
#         i = -i
#
#     summ += i
#
#
# print(summ)

# a,b,c = map(float, input().split())
#
# summ = a + b + c
#
# print(round(summ/3))
#
# a = round(a)
# b = round(b)
# c = round(c)
#
# summ = a + b + c
# # print(round(summ/3))
#
# arr = list(map(int, input().split()))
# for i in range(len(arr)-1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     if i == 4:
#         break
#
# print(*arr)

# a, b, c = map(int, input().split())
#
# num = a * b * c
#
# num = str(num)
#
# result = 1
# for i in num:
#     i = int(i)
#     if i != 0:
#         result *= i
#
# print(result)


# def square(n):
#     start = 1
#     for _ in range(n):
#         for _ in range(n):
#             print(start, end=' ')
#             start += 1
#         print()
# square(int(input()))

# n = int(input())
# result = 1
# def recur(n, result):
#
#     result *= n
#     if n == 1:
#         print(f'{n}! = {n}')
#         return result
#
#     else:
#         print(f'{n}! = {n} * {n - 1}!')
#         return recur(n-1, result)
#
# print(recur(n, result))








MSG_FORMAT = "{} : {} -> {}"


def move(N, start, to):
    print(MSG_FORMAT.format(N, start, to))



# 출발점, 도착점, 경유점
# start에서 via를 거쳐 to로 총 N개의 원반을 운반할 때 각 이동과정은?
def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)




hanoi(int(input()), '1', '3', '2')
