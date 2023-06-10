array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개 남으면 종료
        return
    pivot = start # 호어 분할은 피벗이 첫 번째 데이터
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 떄까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈린다면 작은 데이터와 피벗 자리 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
        
        # 분할 수 왼쪽과 오른쪽에서 각각 정렬
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)
        
# quick_sort(array, 0, len(array) - 1)
# print(array)
    

#복습
def hoare_quick_sort(array, start, end): # array - 데이터, start - 시작할 index위치, 마지막 index위치
    if start >= end:
        return 
    pivot = start # 호어 분할은 가장 첫 번쨰 데이터를 피벗으로 설정
    left = start + 1 #왼쪽에 올 데이터 (피벗과 비교해 큰 데이터를 찾음)
    right = end # 오른쪽에 올 데이터 (피벗과 비교해 작은 데이터를 찾음)

    while left <= right: # index가 왼쪽이 오른쪽보다 적거나 같을 때까지 반복
        while left <= end and array[left] <= array[pivot]: # 피벗보다 큰 데이터를 찾을 때까지 반복
            print('array[left]:', array[left])
            left += 1 # 찾지 못하면 오른쪽으로 한칸이동
        while right > start and array[right] >= array[pivot]: # 피벗보다 작을 데이터를 찾을 때까지 반복
            print('array[right]:', array[right])
            right -= 1 # 찾지 못하면 왼쪽으로 한칸이동
        if left > right: # 피벗보다 왼쪽에서 작은, 오른쪽에서 큰 데어틀 찾지 못 할경우(엇갈릴 경우)
            array[right], array[pivot] = array[pivot], array[right] # 작은 데이터와 피벗 위치 교체
            print('array[right]:', array[right], 'array[pivot]:', array[pivot])
        else:
            array[left], array[right] = array[right], array[left] # 왼쪽과 오른쪽 데이터 교체
            print('array[left]:', array[left], 'array[right]:', array[right])

    hoare_quick_sort(array, start, right - 1) # 분할 후 각각 호어정렬 진행
    hoare_quick_sort(array, right + 1, end)

hoare_quick_sort(array, 0, len(array) - 1)
print(array)