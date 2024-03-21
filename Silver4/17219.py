import sys

n, m = map(int, sys.stdin.readline().split())

password = {}
for _ in range(n):
    site, pw = sys.stdin.readline().split()
    password[site] = pw

for _ in range(m):
    print(password[sys.stdin.readline().strip()])
