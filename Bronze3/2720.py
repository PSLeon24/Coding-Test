coin = [25, 10, 5, 1]
money = []

n = int(input())

# charges = [0, 0, 0, 0]

for _ in range(n):
    money.append(int(input()))

for i in range(n):
    charges = [0, 0, 0, 0]
    for j in range(4):
        charges[j] = money[i] // coin[j]
        money[i] %= coin[j]

    print(*charges)
