# Number Pattern Generator

n = int(input("Enter n: "))

print("\n1. Right Triangle")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n2. Inverted Triangle")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n3. Pascal's Triangle")
for i in range(n):
    num = 1

    # spaces
    for s in range(n - i - 1):
        print(" ", end=" ")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()

print("\n4. Prime Numbers up to", n)

for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")