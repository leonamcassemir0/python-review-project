def printHandshakes(people):

    numberOfHandshakes = 0

    for i in range(0, len(people) - 1):
        for j in range(i + 1, len(people)):
            print(people[i], 'shakes hands with', people[j])
            numberOfHandshakes += 1

    return numberOfHandshakes


print(printHandshakes(['Alice', 'Bob']))
print(printHandshakes(['Alice', 'Bob', 'Carol']))
print(printHandshakes(['Alice', 'Bob', 'Carol', 'David'])) 
