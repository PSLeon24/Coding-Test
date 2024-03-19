import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
deque = deque([i for i in range(1, n + 1)])
answer = []
while deque:
    for _ in range(k - 1):
        deque.append(deque.popleft())
    answer.append(deque.popleft())
print("<" + ", ".join(map(str, answer)) + ">")
