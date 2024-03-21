# Graph
computers = int(input())
networks = int(input())
graph = [[] for i in range(computers + 1)]
visited = [False] * (computers + 1)

for i in range(networks):  # 양방향 그래프 생성
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(visited.count(True) - 1)  # 1번 컴퓨터는 제외
