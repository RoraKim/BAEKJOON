
n = int(input())  # 분해합을 입력값으로 받음

def divsum(n):
    result = n
    while n >= 10:
        result += n % 10
        n = n // 10
    result += n
    return result

for i in range(1, n):
    if divsum(i) == n:
        print(i)
        break

else:
    print(0)






#
# for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
#     num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
#     num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
#     # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
#     if num_sum == n:
#         print(i)
#         break
#     if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
#         print(0)
#




# a = 1
# b = 9
# c = 8
#
# n = (100 * a) + (10 * b) + c + a + b + c
# 101 * a + 11 * b + 2 * c = n
# 216 - 6
# 210 , 6
# 209, 1, 6
# 207, 2, 1, 6