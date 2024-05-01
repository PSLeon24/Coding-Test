def fibonacci(n):
    if n == 0:
        print(0, end="")
        return 0
    elif n == 1:
        print(1, end="")
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


L = [0, 1]
for i in range(41):
    L.append(L[-1] + L[-2])
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(1, 0)
    else:
        print(L[n - 1], L[n])
