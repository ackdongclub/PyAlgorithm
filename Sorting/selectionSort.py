array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 숫자의 위치
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j # 가장 작은 숫자의 위치 보다 j가 더 작으면 가장 작은 인덱스의 위치가 변경된다
            
    array[i], array[min_index] = array[min_index], array[i] # 스와프: 특정 리스트가 주어졌을 때 두 변수의 우치를 변경하는 작업
print(array)
