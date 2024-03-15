import sys


def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    cnt = 0

    for i in range(n + 1, 2 * n + 1):
        if isPrime(i):
            cnt += 1

    print(cnt)
