n, m = map(int, input().split()) # N = 행, M = 열

result = 0
for i in range(n):
   data = list(map(int, input().split()))
   min_value = min(data) # 입력하는 행 중 가장 작은 숫자들만 찾는다
   #print(min_value) 
   result = max(result, min_value) # 가장 작은 숫자들 중 가장 큰 값을 찾는다
print(result)
