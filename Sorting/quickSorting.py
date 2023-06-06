array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개 남으면 종료
        return
    pivot = start # 호어 분할은 피벗이 첫 번째 데이터
    left = start + 1
    right = end
    while left <= right:
        # 피벟보다 큰 데이터를 찾을 때까지 반복
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
        
quick_sort(array, 0, len(array) - 1)
print(array)
    