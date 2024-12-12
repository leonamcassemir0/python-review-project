def mergeTwoLists(list1, list2):
    result = []
    i1 = 0
    i2 = 0

    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] < list2[i2]:
            result.append(list1[i1])
            i1 += 1
        else:
            result.append(list2[i2])
            i2 += 1

    if i1 < len(list1):
        for j in range(i1, len(list1)):
            result.append(list1[j])
    if i2 < len(list2):
        for j in range(i2, len(list2)):
            result.append(list2[j])

    return result


print(mergeTwoLists([1, 3, 6], [5, 7, 8, 9]))
print(mergeTwoLists([1, 2, 3], [4, 5]))
print(mergeTwoLists([4, 5], [1, 2, 3]))
print(mergeTwoLists([2, 2, 2], [2, 2, 2]))
print(mergeTwoLists([1, 2, 3], []))
print(mergeTwoLists([], [1, 2, 3]))