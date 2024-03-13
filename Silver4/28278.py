import sys

n = int(sys.stdin.readline())
commands = []
stack = []

for _ in range(n):
    new = sys.stdin.readline().split()
    commands.append(new)

for command in commands:
    if len(command) >= 2:
        if command[0] == "1":
            stack.append(command[1])
    if command[0] == "2":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if command[0] == "3":
        print(len(stack))
    if command[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if command[0] == "5":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
