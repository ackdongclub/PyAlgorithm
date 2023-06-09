INF = 9999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# -----------------------------------------

graph = [[] for i in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리))
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

# DFS Algorithm
def dfs(graph, v, visited):
    visited[v] = True # 현재 방문한 노드
    print(v, end='')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    []
    , [2, 3, 8]
    , [1, 7]
    , [1, 4, 5]
    , [3, 5]
    , [3, 4]
    , [7]
    , [2, 6, 8]
    , [1, 7]
]
    
visited = [False] * 9
    
dfs(graph, 1, visited)