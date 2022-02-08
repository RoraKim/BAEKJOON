import math
r = int(input())
taxi = ((r ** 2)**0.5) ** 2

print(round((r ** 2) * math.pi, 6))
print(f'{taxi * 2:.6f}')