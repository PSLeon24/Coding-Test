import sys

input = sys.stdin.readline

n = int(input())
paper = [[0] * 100 for _ in range(100)]

for _ in range(n):
    w, h = map(int, input().split())
    for i in range(h, h + 10):
        for j in range(w, w + 10):
            paper[i][j] = 1

result = 0
for k in range(100):
    result += paper[k].count(1)

print(result)
