def fib(num):
    if dp[num] == -1:
        dp[num] = fib(num - 1) + fib(num - 2)

    return dp[num]


num = int(input())
dp = [-1] * 100
dp[0] = 0
dp[1] = 1
print(fib(num))
