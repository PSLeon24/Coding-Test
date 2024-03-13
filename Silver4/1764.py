n, m = map(int, input().split())
dict = {}
cnt = 0
result = []

for _ in range(n + m):
    new = input()
    if new in dict:
        dict[new] += 1
    else:
        dict[new] = 1

for key, value in dict.items():
    if value >= 2:
        result.append(key)
        cnt += 1

result.sort()
print(cnt)
for i in result:
    print(i)
