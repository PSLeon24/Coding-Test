import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

k = int(sys.stdin.readline())
for _ in range(k):
    start, end = map(int, sys.stdin.readline().split())
    print(sum(numbers[start - 1 : end]))
