import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
cnt = 0

graph = [input().rstrip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global cnt
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == "P":
                cnt += 1
            if graph[nx][ny] == "X":
                continue
            visited[nx][ny] = True
            queue.append([nx, ny])


for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            bfs(i, j)
if cnt == 0:
    print("TT")
else:
    print(cnt)
