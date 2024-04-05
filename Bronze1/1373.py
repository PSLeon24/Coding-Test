decimal = list(input())
if len(decimal) % 3 != 0:
    decimal = [0] * (3 - len(decimal) % 3) + decimal

octal = []
for i in range(0, len(decimal), 3):
    octal.append(int(decimal[i]) * 4 + int(decimal[i + 1]) * 2 + int(decimal[i + 2]))

print(*octal, sep="")
