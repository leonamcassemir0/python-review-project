def getCostOfCoffee(numbersOfCoffee, priceOfCofee):
    total = numbersOfCoffee * priceOfCofee

    if numbersOfCoffee > 8:
        total -= (numbersOfCoffee // 8) * priceOfCofee
    
    return total


print(getCostOfCoffee(7, 2.50))
print(getCostOfCoffee(8, 2.50))
print(getCostOfCoffee(9, 2.50))
print(getCostOfCoffee(10, 2.50))

for i in range(1, 4):
    print(getCostOfCoffee(0, i))
    print(getCostOfCoffee(8, i))
    print(getCostOfCoffee(9, i))
    print(getCostOfCoffee(18, i))
    print(getCostOfCoffee(19, i))
    print(getCostOfCoffee(30, i))