#이진 탐색
#일단 정렬을 한다
# 중앙값을 찾고 내가 찾고자하는 값이
#중앙보다 왼쪽인지, 오른쪽인지 찾는다
# 해당하는 곳으로 간다.

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)

def binary(start, end, search, arr):
    if start > end:
        print(0)
        return

    mid = (start + end) // 2
    if search == arr[mid]:
        print(1)
        return

    elif search < arr[mid]:
        binary(start, mid -1, search, arr)

    else:
        binary(mid + 1, end, search, arr)




m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    search = num
    start = 0
    end = n - 1
    binary(start, end, search, arr)

