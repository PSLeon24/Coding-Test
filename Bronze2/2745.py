n, b = input().split()
str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = n[::-1]
result = 0
for i, n in enumerate(n):
    result += str.index(n) * (int(b) ** i)

print(result)
