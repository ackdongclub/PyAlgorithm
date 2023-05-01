def problem1():
    n, m ,k = map(int, input().split()) # N, M, K 값을 Int형으로 받아온다
    data = list(map(int, input().split())) # 데이터

    data.sort() # 값을 정렬한다(오름차순)
    first = data[n - 1] # 첫 번째로 큰 숫자를 가져옴
    second = data[n - 2] # 두 번째로 큰 숫자를 가져옴

    result = 0

    while True: # 무한 반복
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1 # 한번 돌면 m의 회수를 줄임
        if m == 0:
            break
        result += second
        m -=1
        
    print(result)

def problem2():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    
    data.sort()
    first = data[n - 1]
    second = data[n - 2]
    
    count = int(m / (k + 1)) * k #전체가 반복되는 횟수와 같은 수가 몇번 반복되는지 확인
    count += m % (k + 1) # 완전히 나누어지지 않는 경우를 대비해 나머지흫 더 해줌
    
    result = 0
    
    result += count * first # 가장 큰수가 반복되는 횟수에 값을 곱해줌
    result += (m - count) * second # 전체 숫자에서 가장 큰 값의 개수를 뺀 나머지에 두 번째로 큰 값을 곱한 값을 더한다
    
    print(result)
    
problem2()
            
    
