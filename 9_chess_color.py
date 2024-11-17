def getChessSquareColor(column, row):
    if column >= 8 or row >= 8:
        return ' '
    else:
        if column % 2 == row % 2:
            return 'White'
        else:
            return 'Black'


print(getChessSquareColor(1, 1)) 
print(getChessSquareColor(2, 1)) 
print(getChessSquareColor(1, 2)) 
print(getChessSquareColor(7, 7)) 
print(getChessSquareColor(0, 8)) 
print(getChessSquareColor(2, 9))
