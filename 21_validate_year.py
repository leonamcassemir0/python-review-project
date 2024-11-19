import leap_year


def isValidDate(year, month, day):
    if not 1 <= month <= 12:
        return False

    if leap_year.isLeapYear(year) and month == 2 and day == 29:
        return True

    if month in (1, 3, 5, 7, 8, 10, 12) and not 1 <= day <= 31:
        return False
    elif month in (4, 6, 9, 11) and not 1 <= day <= 30:
        return False
    elif month == 2 and not (1 <= day <= 28):
        return False

    return True


print(isValidDate(1999, 12, 31))
print(isValidDate(2000, 2, 29))
print(isValidDate(2001, 2, 29))
print(isValidDate(2029, 13, 1))
print(isValidDate(1000000, 1, 1))
print(isValidDate(2015, 4, 31))
print(isValidDate(1970, 5, 99))
print(isValidDate(1981, 0, 3)) 
print(isValidDate(1666, 4, 0))
