import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    white = []
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        white.append([y, x])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
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
                if graph[nx][ny] == 0:
                    continue
                visited[nx][ny] = True
                queue.append([nx, ny])

    for i in white:
        if not visited[i[0]][i[1]]:
            bfs(i[0], i[1])
            cnt += 1
    print(cnt)
