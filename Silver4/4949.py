import sys

input = sys.stdin.readline

stack = []

while True:
    string = input().rstrip()
    if string == ".":
        break

    for i in string:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] == "[":
                print("no")
                break
            elif stack[-1] == "(":
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(":
                print("no")
                break
            elif stack[-1] == "[":
                stack.pop()
    else:
        if not stack:
            print("yes")
        else:
            print("no")
    stack.clear()
