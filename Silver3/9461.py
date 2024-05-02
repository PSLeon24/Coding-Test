import sys

input = sys.stdin.readline

T = int(input())

P = []

for _ in range(T):
    P.append(int(input()))

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for i in P:
    print(dp[i])
