n, m = map(int, input().split())

set1 = set()
for _ in range(n):
    set1.add(input())

cnt = 0
for _ in range(m):
    str = input()
    if str in set1:
        cnt += 1

print(cnt)
