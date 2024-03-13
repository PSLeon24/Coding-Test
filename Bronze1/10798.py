array = []
length = []

for i in range(5):
    array.append(list(str(input())))
    length.append(len(array[i]))

new = ""
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            new += array[j][i]

print(new)
