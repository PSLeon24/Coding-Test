import sys


def dfs():
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return
    else:
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                dfs()
                stack.pop()
                visited[i] = False


n, m = map(int, sys.stdin.readline().split())
stack = []
visited = [False] * (n + 1)

dfs()
