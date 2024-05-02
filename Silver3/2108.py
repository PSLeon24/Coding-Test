import sys
import statistics

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

numbers.sort()
print(round(sum(numbers) / n))
if n % 2 == 0:
    print((numbers[n // 2] + numbers[n // 2 + 1]) // 2)
else:
    print(numbers[n // 2])

mode = statistics.mode(numbers)
modes = statistics.multimode(numbers)
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

print(numbers[-1] - numbers[0])
