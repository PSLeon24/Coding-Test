row = 0
col = 0
array = []
maximum = []

for i in range(9):
    array.append(list(map(int, input().split())))
    maximum.append(max(array[i]))

maximum = max(maximum)
for i in array:
    if maximum in i:
        row = array.index(i) + 1
        col = i.index(maximum) + 1

print(maximum)
print(row, col)
