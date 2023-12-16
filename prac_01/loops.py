for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, -1, -1):
    print(i, end=' ')
print()

# c.
stars_number = int(input("Number of stars: "))
for i in range(0, stars_number):
    print("*", end=' ')
print()

# d.
stars_line = int(input("Number of stars: "))
for i in range(0, stars_line):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()
