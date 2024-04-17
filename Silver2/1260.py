from collections import deque

n, m, v = map(int, input().split())
# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # A번 정점과 B번 정점 사이에 간선이 존재
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()


def dfs(graph, v, visited):
    visited[v] = True  # 방문 처리
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True  # 방문 처리

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
