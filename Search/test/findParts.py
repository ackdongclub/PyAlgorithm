def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 # 중간 지점 설정
        if array[mid] == target:
            return mid # 중간 데이터와 타겟 데이터가 동일하면 중간 인덱스 반환
        elif array[mid] > target: # 중간 데이터가 타겟 데이터보다 크면 왼쪽 확인
            end = mid - 1
        else:
            start = mid + 1 # 타겟 데이터보다 작으면 오른쪽 확인
        return None
    n = int(input()) # 부품 개수 입력
    array = list(map(int, input().split()))
    array.sort() # 이진 탐색은 정렬이 기본조건으로 되어있으므로 정렬을 먼저해줌
    m = int(input()) # 손님이 확인 요청한 부품 개수 입력
    x = list(map(int, input().split()))
    
    for i in x:
        result = binary_search(array, i, 0, n - 1)
        if result != None:
            print('yes', end=' ')
        else:
            print('No', end=' ')
    
        