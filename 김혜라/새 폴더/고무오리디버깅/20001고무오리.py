import sys; sys.stdin = open('20001고무오리.txt',encoding='utf-8')

stack = []
while 1:
    spell = input()
    if spell == '문제':
        stack.append('문제')

    if spell == '고무오리':
        if len(stack) > 0:
            check = stack.pop()
            if check == "문제":
                continue
            # else:
            #     stack.append('문제')
            #     stack.append('문제')
        else:
            stack.append('문제')
            stack.append('문제')

    if spell == '고무오리 디버깅 끝':
        break

if len(stack) == 0:
    print('고무오리야 사랑해')

else:
    print('힝구')
