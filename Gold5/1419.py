import sys

input = sys.stdin.readline

# left, right
l = int(input())
r = int(input())
k = int(input())

# 2 <= k <= 5
"""
k = 2
    - l이 최소 3부터 시작(1 + 2 = 3)
    - n + n + d = 2n + d = 3, 4, 5, 6, ...
k = 3
    - l이 최소 6부터 시작(1 + 2 + 3 = 6)
    - n + n + d + n + 2d = 3n + 3d = 6, 9, 12, 15, ...
k = 4
    - l이 최소 10부터 시작(1 + 2 + 3 + 4 = 10)
    -  n + n + d + n + 2d + n + 3d = 4n + 6d = 10, 14, 18, 22, ...
k = 5
    - l이 최소 15부터 시작(1 + 2 + 3 + 4 + 5 = 15)
    - n + n + d + n + 2d + n + 3d + n + 4d = 5n + 10d = 15, 20, 25, 30, ...
"""

if k == 2:
    print(max(0, r - max(l, 3) + 1))
elif k == 3:
    print(max(0, r // 3 - (max(l, 6) - 1) // 3))
elif k == 4:
    print(max(0, r // 2 - (max(l, 14) - 1) // 2) + (l <= 10 <= r))
elif k == 5:
    print(max(0, r // 5 - (max(l, 15) - 1) // 5))
