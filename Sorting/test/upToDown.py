n = int(input()) # N값 입력 받음

array = [] # 배열 생성

for i in range(n): # N만큼 돈다
    array.append(int(input())) # N개 만큼 array에 값을 넣어준다
    
result = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')