def hansu(num):
    if num < 100:
        result = num

    else:
        result = 99
        for i in range(100, num + 1):
            snum = str(i)
            if int(snum[0]) - int(snum[1]) == int(snum[1]) - int(snum[2]):
                result += 1
                # print(snum[0], snum[1], snum[2])

    return result


print(hansu(int(input())))
