def drawrectangle(column, row):
    for r in range(row):
        for c in range(column):
            print("#", end="")
        print()


print("Retângulo 16x4:")
drawrectangle(16, 4)
print("Retângulo 15x5:")
drawrectangle(15, 5)