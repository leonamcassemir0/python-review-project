import random


def rollDice(dice):
    total = 0
    for i in range(dice):
        total += random.randint(1, 6)
    
    return total


print(rollDice(0))
print(rollDice(1))
print(rollDice(2))
print(rollDice(3))
print(rollDice(1000) != rollDice(1000))
print(1 <= rollDice(1) <= 6)
print(2 <= rollDice(2) <= 12)
print(3 <= rollDice(3) <= 18)
print(100 <= rollDice(100) <= 600)
