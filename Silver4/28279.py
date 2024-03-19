import sys
from collections import deque

n = int(sys.stdin.readline())
commands = []
deque = deque()

for _ in range(n):
    new = sys.stdin.readline().split()
    commands.append(new)

for command in commands:
    if len(command) >= 2:
        if command[0] == "1":
            deque.appendleft(command[1])
        elif command[0] == "2":
            deque.append(command[1])
    if command[0] == "3":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    if command[0] == "4":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    if command[0] == "5":
        length = len(deque)
        print(length)
    if command[0] == "6":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    if command[0] == "7":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    if command[0] == "8":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
