import sys; sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = [list(input())for _ in range(n)]

# print(arr)
lst = []
minn = 10e9
for i in range(n-7):
    for j in range(m-7):
        first_w = 0
        first_b = 0

        #행과 열의 인덱스 번호의 합이 짝수인 경우와 홀수인 경우
        #차지하는 색이 같다.
        for k in range(i, i+8):
            for l in range(j, j +8):
                #행과 열의 인덱스의 합이 짝수라면
                if (k + l) % 2 == 0:
                    #짝수는 다 같이 검은색 이어야 하는데 흰색이 있다면
                    #검은색으로 바꿔줄 것 1 추가
                    if arr[k][l] != 'B':
                        first_b += 1

                    #짝수는 다 같이 흰색이어야 하는데 검은색이 있다면
                    #흰색으로 바꿔줄 것 1 추가
                    if arr[k][l] != 'W':
                        first_w += 1

                #인덱스의 합이 홀수라면
                else:
                    #맨 첫 칸이 white였다면, 인덱스 합이 홀수일때는 항상 b여야함
                    if arr[k][l] != 'B':
                        first_w += 1

                    #맨 첫 칸이 black이었다면, 인덱스 합이 홀수일때는 항상 w여야 함
                    #해당 안되는 값 추가
                    if arr[k][l] != 'W':
                        first_b += 1


        if first_w <= minn:
            minn = first_w

        if first_b <= minn:
            minn = first_b

print(minn)
#         lst.append(first_b)
#         lst.append(first_w)
#
# print(lst)
# print(min(lst))

