import sys; sys.stdin = open('safecracker')

def DFS(L):
    # result = [0] * r
    global final_result
    # global result

    #종료조건
    # 뽑으라고 한 갯수만큼 뽑으면 종료
    #dfs 레벨이 뽑는 갯수와 같으면 종료
    if L == r:
        if result[0] - (result[1]**2) + (result[2]**3) - (result[3]**4) + (result[4]**5) == target:
            # print(result)
            # return result

            final_result.append(result[::1])
            # print(final_result)
            # return

    else:
        for i in range(len(n)):
            #0이라는 것은 해당 값을 가져다 쓰지 않았다는 뜻임
            if checklist[i] == 0:
                result[L] = n[i]
                #체크를 하고
                checklist[i] = 1
                #재귀를 하고 트래버스를 하고
                #재귀의 전에는 전처리를 적어주고
                DFS(L + 1)
                #백트래버스를 할 때는 지워줘라
                #재귀 후처리를 적어줌
                checklist[i] = 0


alpha = list(input().split())
target, *alpha = alpha
target = int(target)
# print(target, type(target))
# print(alpha)

main_lst = []
for i in alpha:
    for j in i:
        # print(ord(j))
        ord_alpha = ord(j) - 64
        # print(ord_alpha)
        main_lst.append(ord_alpha)

# print(main_lst)
n = main_lst
r = 5

global final_result
final_result = []
# global result
result = [0] * r

checklist = [0] * len(n)

DFS(0)

sorted(final_result)
print(final_result[-1])


