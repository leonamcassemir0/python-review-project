def convertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9 / 5) + 32 


def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5 / 9)   


print(convertToCelsius(0))
print(convertToCelsius(180))
print(convertToFahrenheit(0))
print(convertToFahrenheit(100))
print(convertToCelsius(convertToFahrenheit(15)))
