array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0] * (max(array) + 1) # 모든 값을 0으로 초기화 index 0 ~ n + 1까지

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가
    
for i in range(count): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 등장한 횟수만큼 인덱스 출력