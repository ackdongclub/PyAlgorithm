# 재귀함수를 사용한 이진탐색
def binary_search(array, target, start, end):
    if start > end: # 원소가 없으면 none을 리턴
        return None
    mid = (start + end) //2 # 가운데 인덱스
    
    if array[mid] == target:
        return mid # 중간과 찾는 값이 동일하면 mid를 리턴
    elif array[mid] > target:
        end = mid - 1 # 중간 값보다 찾는 값이 더 크면 오른쪽 확인
    else:
        start = mid + 1
    return None

# 원소의 개수와 target을 입력 받는다
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)
    
    