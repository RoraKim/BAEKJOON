import sys; sys.stdin = open('4344.평균은넘겠지.txt')

t = int(input())
for tc in range(t):
    a, *lst = list(map(int, input().split()))
    # print(a)
    # print(lst)
    avg_lst = sum(lst) / len(lst)
    # print(avg_lst)

    cnt = 0
    for i in lst:
        if i > avg_lst:
            cnt += 1

    result = cnt / len(lst) * 100
    print('{:.3f}%'.format(result))
