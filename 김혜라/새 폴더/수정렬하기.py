n = int(input())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

# print(arr)
k = 10000
# arr.sort()
# for i in arr:
#     print(i)


def counting(input_arr, k):
    counting_arr = [0] * (k + 1)
    for i in range(0, len(input_arr)):
        counting_arr[input_arr[i]] += 1
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]

    result_arr = [-1] * len(input_arr)

    for i in range(len(result_arr) - 1, -1, -1):
        counting_arr[input_arr[i]] -= 1
        result_arr[counting_arr[input_arr[i]]] = input_arr[i]

    return result_arr

result_arr = counting(arr, k)
for i in result_arr:
    print(i)



