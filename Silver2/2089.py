n = int(input())
result = ""

if n == 0:
    print(0)
    exit(0)

while n:
    if n % -2:
        result = "1" + result
        n = n // -2 + 1
    else:
        result = "0" + result
        n //= -2

print(result)
