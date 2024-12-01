def commaFormat(number):
    number = str(number)

    if '.' in number:
        fractionalPart = number[number.index('.'):]
        number = number[:number.index('.')]
    else:
        fractionalPart = ''

    triplet = ''
    commaNumber = ''

    for i in range(len(number) - 1, -1, -1):
        triplet = number[i] + triplet

        if len(triplet) == 3:
            commaNumber = triplet + ',' + commaNumber
            triplet = ''

    if triplet != '':
        commaNumber = triplet + ',' + commaNumber

    return commaNumber[:-1] + fractionalPart


print(commaFormat(1))
print(commaFormat(10))
print(commaFormat(100)) 
print(commaFormat(1000)) 
print(commaFormat(10000))
print(commaFormat(100000))
print(commaFormat(1000000)) 
print(commaFormat(10000000)) 
print(commaFormat(1234567890))
print(commaFormat(1000.123456))