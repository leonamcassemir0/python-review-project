def isOdd(num):
    if type(num) == int:
        if num % 2 != 0:
            return True
        else:
            return False
    else:
        return False
    

def isEven(num):
    if type(num) == int:
        if num % 2 == 0:
            return True
        else:
            return False
    else:
        return False


print(isOdd(42))
print(isOdd(9999))
print(isOdd(-10))
print(isOdd(-11))
print(isOdd(3.145))
print(isEven(42))
print(isEven(9999))
print(isEven(-10))
print(isEven(-11))
print(isEven(3.145))
