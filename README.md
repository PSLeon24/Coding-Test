# Coding-Test
5 Problems a Day: Enhancing My Coding Skills with Baekjoon

# 유형별 좋은 문제 정리
## DFS/BFS
- [백준 1012] 유기농 배추
- [백준 1260] DFS와 BFS
- [백준 2178] 미로 탐색
- [백준 2606] 바이러스
- [백준 2667] 단지번호붙이기

# 기본 틀
## DFS/BFS
- DFS

```
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:  
      dfs(graph, i, visited)

dfs(graph, 1, visited)
```

- BFS

```
from collections import deque
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        
bfs(graph, 1, visited)
```

## Statistics

```
import statistics
n = int(input())
numbers = [int(input()) for _ in range(n)]
mode = statistics.mode(numbers) # 최빈값 하나만 뽑을 때
modes = statistics.multimode(numbers) # 최빈값이 여러 개가 의심될 때
```
