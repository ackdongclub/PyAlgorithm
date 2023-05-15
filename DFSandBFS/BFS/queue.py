from collections import deque # 스택과 큐의 장점을 모아 놓은 라이브러리. 데이터를 넣고 빼는 속도가 효율적이며 queue보다 사용하기 편하다.

# 큐 구현을 위한 라이브러리
Queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
Queue.append(5)
Queue.append(2)
Queue.append(3)
Queue.append(7)
Queue.popleft()
Queue.append(1)
Queue.append(4)
Queue.popleft()

print(Queue) # 들어온 순서대로 출력
Queue.reverse() # 역순으로 변환
print(Queue)

for i in range(len(Queue)):
    print(Queue[i])