import sys; sys.stdin = open('2161카드1.txt')
n = int(input())
queue = []

for i in range(1, n + 1):
    queue.append(i)
# print(queue)
while len(queue) > 1:
    print(queue.pop(0), end=' ')
    back = queue.pop(0)
    queue.append(back)

print(queue.pop(0), end=' ')


