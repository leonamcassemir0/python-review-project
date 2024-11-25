def drawTriangle(row):
    for r in range(row):
        print(" " * (row - (r + 1)) , "#" * ((r * 2) + 1))


print("Triangulo com 3 niveis:")
drawTriangle(3)
print()
print("Triangulo com 8 niveis:")
drawTriangle(8)