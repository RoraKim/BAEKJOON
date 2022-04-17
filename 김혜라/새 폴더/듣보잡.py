

# def quick_sort(array, start, end):
#     if start >= end: # 원소가 1개인 경우 종료
#         return
#     pivot = start # 피벗은 첫 번째 원소
#     left = start + 1
#     right = end
#     while(left <= right):
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while(left <= end and array[left] <= array[pivot]):
#             left += 1
#         # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while(right > start and array[right] >= array[pivot]):
#             right -= 1
#         if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#         else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)
#
#


n, m = map(int, input().split())
deddo = []
bodo = []

for i in range(n):
    ded = input()
    deddo.append(ded)

for j in range(m):
    bo = input()
    bodo.append(bo)

debbojabs = list(set(deddo) & set(bodo))
print(len(debbojabs))
debbojabs.sort()
for debbojab in debbojabs:
    print(debbojab)


#
# print(arr)
# arr = sorted(arr)
# print(len(arr))
# for j in range(n+m):
#     if arr.count(arr[j]) == 2:
#         print(arr[j])


# print(result)
# result.sort()
# print(len(result))
# for j in result:
#     print(j)
