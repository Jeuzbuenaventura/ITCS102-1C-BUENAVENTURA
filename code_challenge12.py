
n = 6

for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for x in range(i, 0, -1):
        print(x, end=" ")
    for x in range(2, i + 1):
        print(x, end=" ")
    print()