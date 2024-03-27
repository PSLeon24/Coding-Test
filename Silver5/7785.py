lst = []

for _ in range(int(input())):
    name, status = input().split()
    if status == "enter":
        lst.append(name)
    elif status == "leave":
        lst.remove(name)

lst.sort(reverse=True)

print("\n".join(lst))
