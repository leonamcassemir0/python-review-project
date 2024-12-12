pennies = 1
nickels = 5
dimes = 10
quarters = 25



def changeMaker(value):
    change = {}
    if value >= 25:
        change['quarters'] = value // 25
        value = value % 25
    if value >= 10:
        change['dimes'] = value // 10
        value = value % 10
    if value >= 5:
        change['nickels'] = value // 5
        value = value % 5
    if value >= 1:
        change['pennies'] = value // 1
    
    return change


print(changeMaker(30))
print(changeMaker(45))
print(changeMaker(1))
print(changeMaker(5))
print(changeMaker(10))
print(changeMaker(25))
