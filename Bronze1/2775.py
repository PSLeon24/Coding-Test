import sys

T = int(sys.stdin.readline())


def get_people(k, n):
    f0 = [x for x in range(1, n + 1)]
    for k in range(k):
        for i in range(1, n):
            f0[i] += f0[i - 1]
    return f0[-1]


for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(get_people(k, n))
