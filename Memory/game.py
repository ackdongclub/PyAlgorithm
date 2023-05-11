n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
# d배열의 0번째에 m을 곱함 그리고 0~n까지 돈다.
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문
