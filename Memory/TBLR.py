n = int(input())
x, y = 1, 1
plans = input().split()

# 이렇게 선언할 수도 있군...
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans: # 입력 받는 값을 차례대로 넣어준다
    for i in range(len(move_types)): 
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n: # 행을 벗어나면 무시됨
            continue
        x, y = nx, ny
print(x, y)