import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(list(map(int, sys.stdin.readline().split())))
stack = []

order = 1

while queue:
    if queue[0] == order:
        queue.popleft()
        order += 1
    elif queue[0] != order:
        stack.append(queue.popleft())

    while stack:
        if stack[-1] == order:
            stack.pop()
            order += 1
        else:
            break

if (order - 1) == n:
    print("Nice")
else:
    print("Sad")
