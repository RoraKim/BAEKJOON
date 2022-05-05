import sys
input = sys.stdin.readline

count = [0] * 10001

for i in range(int(input())):
    count[int(input())] += 1

for i in range(len(count)):
    while count[i]>0:
        print(i)
        count[i] -= 1

