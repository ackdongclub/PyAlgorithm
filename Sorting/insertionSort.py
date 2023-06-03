array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하면서 반복
        if array[j] < array[j - 1]: # 자리 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자신보다 작으면 해당 위치에 멈춤
            break
        
print(array)