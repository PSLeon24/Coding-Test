import sys

input = sys.stdin.readline

n = int(input())

stack = []
answer = []
flag = True
cnt = 1

for _ in range(n):
    x = int(input())
    while cnt <= x:
        stack.append(cnt)
        answer.append("+")
        cnt += 1
    if stack[-1] == x:
        stack.pop()
        answer.append("-")
    else:
        flag = False
        break

if not flag:
    print("NO")
else:
    print(*answer, sep="\n")
