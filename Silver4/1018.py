n, m = map(int, input().split())

W = []  # White
B = []  # Black
len_W, len_B = 0, 0

status = []
for _ in range(n):
    status.append(list(str(input())))

for i in range(n):
    for j in range(m):
        if status[i][j] == "W":
            W.append(status[i][j])
        elif status[i][j] == "B":
            B.append(status[i][j])

len_W = len(W)
len_B = len(B)

print(len_W, len_B)
