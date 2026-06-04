n = int(input("Enter a number n: "))

print("\n1. Right Triangle of Stars")
for i in range(1, n + 1):
    print("*" * i)

print("\n2. Inverted Triangle of Numbers")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n3. Pascal's Triangle")
triangle = []

for i in range(n):
    row = [1]
    if triangle:
        last_row = triangle[-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)

    triangle.append(row)

for row in triangle:
    print(" " * (n - len(row)), end="")
    for num in row:
        print(num, end=" ")
    print()

print("\n4. Prime Numbers up to n")
for num in range(2, n + 1):
    is_prime = True

    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()