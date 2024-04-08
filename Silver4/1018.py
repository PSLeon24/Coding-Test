import sys

input = sys.stdin.readline
n, m = map(int, input().split())

# Good chess board
board_1 = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
]

board_2 = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
]

board = []
for _ in range(n):
    board.append(list(map(str, input().rstrip())))

results = []

for i in range(n - 7):
    for j in range(m - 7):
        result_1 = 0
        result_2 = 0
        temp = [row[j : j + 8] for row in board[i : i + 8]]
        for k in range(8):
            for h in range(8):
                if temp[k][h] == board_1[k][h]:
                    result_1 += 1
                if temp[k][h] == board_2[k][h]:
                    result_2 += 1
        results.append(min(result_1, result_2))

print(min(results))
