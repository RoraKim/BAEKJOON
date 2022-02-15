t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    arr = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    for i in range(k + 1):
        # print(i)
        for j in range(n + 1):

            if i == 0:  
                arr[i][j] = j
        
    # print(arr)

    for i in range(1, k + 1):
        for j in range(1, n+1):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    print(arr[k][n])
