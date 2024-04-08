import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
while True:
    if n <= 0:
        break
    cnt += n // 5
    n //= 5

print(cnt)
