def draw_border(width, height):
    print("+", end="")
    for w in range(width - 2):
        print("-", end="")
    print("+")

    count = width - 2
    for h in range(height - 2):
        print("|", end=" "*count)
        print("|")

    print("+", end="")
    for w in range(width - 2):
        print("-", end="")
    print("+")


print("Border 16x4:")
draw_border(16, 4)
print("Border 20x5:")
draw_border(20, 5)
