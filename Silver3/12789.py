import sys

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
stack = []
while True:
    if len(line) == 0:
        break
    if line[0] != min(line):
        stack.append(line.pop(0))
    else:
        line.pop(0)

if len(line) == 0:
    print("Nice")
else:
    print("Sad")
