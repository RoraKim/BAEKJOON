N = int(input())
for _ in range(N):
    result = input()

    score = 0
    cnt = 0
    for i in range(len(result)):

        if result[i] == "O":
            cnt += 1

        elif result[i] == "X":
            for j in range(1, 1 + cnt):
                score += j
            cnt = 0

    if result[-1] == "O":
        for k in range(1, 1 + cnt):
            score += k



    print(score)


