from collections import deque

n = int(input())
commands = []

for _ in range(n):
    new = input().split()
    commands.append(new)

queue = deque()
for command in commands:
    if len(command) >= 2:
        if command[0] == "push_front":
            queue.appendleft(command[1])
    if len(command) >= 2:
        if command[0] == "push_back":
            queue.append(command[1])
    if command[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    if command[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    if command[0] == "size":
        print(len(queue))
    if command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
