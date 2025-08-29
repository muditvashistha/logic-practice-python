x = 5
for i in range(x):
    spaces = " " * (x - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
# Reverse hill pattern
x = 5
for i in range(x):
    spaces = " " * i
    stars = "*" * (2 * (x - i) - 1)
    print(spaces + stars)


