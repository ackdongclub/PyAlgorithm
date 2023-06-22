def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 데이터를 찾으면 중간 값 반환
        if array[mid] == target:
            return mid
        # 중간 값보다 찾는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        