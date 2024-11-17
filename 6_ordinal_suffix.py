def ordinalSuffix(number):
    numberStr = str(number)
    if number % 100 in (11, 12, 13):
        return numberStr + 'th'
    if number % 10 == 1:
        return numberStr + 'st'
    if number % 10 == 2:
        return numberStr + 'nd'
    if number % 10 == 3:
        return numberStr + 'rd'
    
    return numberStr + 'th'


print(ordinalSuffix(0))
print(ordinalSuffix(1))
print(ordinalSuffix(2))
print(ordinalSuffix(3))
print(ordinalSuffix(4))
print(ordinalSuffix(10))
print(ordinalSuffix(11))
print(ordinalSuffix(12))
print(ordinalSuffix(13))
print(ordinalSuffix(14))
print(ordinalSuffix(101))
