import sys; sys.stdin = open('2669단지번호붙이기.txt')
#dfs로 최대로 탐색한 것이 바뀔 때 마다 단지 수 증가
#각 dfs안에서 cnt한 값을 저장


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


def dfs(x, y):
    global cnts

    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False

    if arr[x][y] == 1:
        cnts += 1
        arr[x][y] = 0
        # print(cnt)
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        # cnts_arr.append(cnts)
        return True
    return False

cnts = 0
cnts_arr = []
num = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            cnts_arr.append(cnts)
            num += 1
            cnts = 0

print(num)
cnts_arr.sort()
for i in cnts_arr:
    print(i)
# print(cnts_arr)












