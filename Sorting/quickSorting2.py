array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소를 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트 (1부터 마지막까지)
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))
    
# 호어정렬2 복습 - 반복을 더 많이 하므로 비효율적이지만 더욱 직관적인 코딩
def hoare_sort_2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    print(hoare_sort_2(left_side) + [pivot] + hoare_sort_2(right_side)) # 재귀호출로 분할했던 왼쪽 정렬
    return hoare_sort_2(left_side) + [pivot] + hoare_sort_2(right_side) # 재귀호출로 분할했던 오른쪽 정렬
print(hoare_sort_2(array))
        