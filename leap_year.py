def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

print(isLeapYear(1999)) 
print(isLeapYear(2000)) 
print(isLeapYear(2001)) 
print(isLeapYear(2004)) 
print(isLeapYear(2100)) 
print(isLeapYear(2400))
