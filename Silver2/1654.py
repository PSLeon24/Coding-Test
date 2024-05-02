import sys

input = sys.stdin.readline
k, n = map(int, input().split())

lan = [int(input()) for _ in range(k)]
sum_lan = sum(lan)

start = 1
end = sum_lan // n
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
