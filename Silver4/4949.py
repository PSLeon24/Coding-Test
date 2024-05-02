sentence = []
stack = []

while True:
    string = input().rstrip()
    sentence.append(string)
    if string == ".":
        break

for i in sentence:
    for j in i:
        if j == "(" or j == "[":
            stack.append(j)
        elif j == ")":
            if not stack or stack[-1] == "[":
                print("no")
                break
            elif stack[-1] == "(":
                stack.pop()
        elif j == "]":
            if not stack or stack[-1] == "(":
                print("no")
                break
            elif stack[-1] == "[":
                stack.pop()
        elif j == ".":
            if not stack:
                print("yes")
            else:
                print("no")
    else:
        if not stack:
            print("yes")
        else:
            print("no")
