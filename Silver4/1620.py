import sys

input = sys.stdin.readline

n, m = map(int, input().split())

poketmon = {}

for i in range(1, n + 1):
    name = input().rstrip()
    poketmon[name] = str(i)
    poketmon[i] = name

for _ in range(m):
    call = input().rstrip()
    if call.isnumeric():
        print(poketmon[int(call)])
    else:
        print(poketmon[call])
