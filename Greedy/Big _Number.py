n, m ,k = map(int, input().split()) # N, M, K 값을 Int형으로 받아온다
data = list(map(int, input().split())) # 데이터

data.sort() # 값을 정렬한다(오름차순)
first = data[n - 1] # 첫 번째로 큰 숫자를 가져옴
second = data[n - 2] # 두 번째로 큰 숫자를 가져옴

result = 0

while True: #무한 반복
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -=1
    
print(result)
