def problem1():
    n, k = map(int, input().split())
    result = 0

    # n이 k 이상이면 계속 반복
    while n >= k:
        while n % k != 0: # k로 n을 나눴을 때 나누어 떨어지지 않는다면 n이 1이 될때까지 1 빼기
            n -= 1
            result += 1
        n //= k # 나누기
        result += 1
    print(result)
        
    while n > 1:
        n -= 1
        result += 1
    print(result)
    
def problem2():
    n, k = map(int, input().split())
    result = 0
  
    while True:
        # n이 k의 배수일 경우에만 적용됨
        target = (n // k) * k
        result += n - target
        
        n = target
        if n < k:
            break
        result += 1
        n //= k
        
    result += (n - 1)
    print(result)
    
problem2()