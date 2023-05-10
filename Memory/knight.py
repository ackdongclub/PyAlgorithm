answer = input()
row = int(answer[1])
column = int(ord(answer[0])) - int(ord('a')) + 1 # ord = 유니코드 변환 함수
# 왜 마이너스가 안 나오나 했더니 빼기하고 더하기를 마지막에 해주네...
#print('row: ', row)
#print('column: ', int(ord(answer[0])), '-', int(ord('a')) + 1, int(ord(answer[0])) - int(ord('a')) + 1  )

# 나이트가 이동할 수 있는 8가지 방법
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 이동이 가능하면 count
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8: # 좌표안에 들어있는 경우라면
        result += 1 # 경우의 수 추가
print(result)