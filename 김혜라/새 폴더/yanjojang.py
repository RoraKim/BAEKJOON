t = int(input())



for _ in range(t):
    schools = dict()
    n = int(input())
    for _ in range(n):
        school, alco = input().split()
        alco = int(alco)

        try:
            schools[school] += alco

        except:
            schools[school] = alco

    print(schools)

    max = -1
    for key, val in schools.items:
        if val > max:
            max = val

    for key, val in schools.items:
        if val == max:
            print(key)

