import random


def shuffle(values):
    for i in range(len(values)):
        swapIndex = random.randint(0, (len(values) - 1))
        values[i], values[swapIndex] = values[swapIndex], values[i]

    return values


test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(shuffle(test))
