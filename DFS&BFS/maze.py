from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
#     상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque() # 큐 사용
    queue.append((x, y)) # x, y를 큐에 삽입
    while queue: 
        x, y = queue.popleft() # 선입선출
        for i in range(4): # 4방향
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표를 벗어나면 무시
            if nx >= n or nx <= 0 or ny >= m or ny <= 0:
                continue
            if graph[nx][ny] == 0: # 벽일경우 무시
                continue
            if graph[nx][ny] == 1: # 처음 도는 곳이면 표시
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        return graph[n - 1][m - 1] # 최단거리 반환
    print(bfs(0, 0))