N = int(input())

cards = [str(i) for i in range(1, N+1)]
result = ''

while 1:
    result += cards.pop(0)+' '
    if not cards:
        break
    n = cards.pop(0)
    cards += [n]
result = result
print(result)