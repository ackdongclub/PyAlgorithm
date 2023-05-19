stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5) # append는 리스트의 가장 뒷쪽에 데이터 삽입
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # pop은 리스트 가장 뒷쪽의 데이터 삭제
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단부터 출력
print(stack[::-1]) # 최상단 원소부터 출력