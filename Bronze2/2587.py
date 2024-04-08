values = []

for i in range(5):
    values.append(int(input()))

mean = sum(values) / 5
values.sort()
if len(values) % 2 == 0:
    median = (values[len(values) // 2 - 1] + values[len(values) // 2]) / 2
else:
    median = values[len(values) // 2]

print(int(mean))
print(int(median))
