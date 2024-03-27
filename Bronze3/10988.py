string = list(input())
stack = string[::-1]

for i in range(len(string)):
    if string[i] != stack[i]:
        print(0)
        break
    elif i == len(string) - 1:
        print(1)
