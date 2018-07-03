def binarySearch(myItem, myList):
    found = False
    bottom = 0
    top = len(myList) - 1
    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if myList[middle] == myItem:
            found = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            top = middle - 1
    return found


if __name__ == "__main__":
    item = int(input("Enter any number: "))
    list = [1, 2, 3, 4, 5, 6, 7, 9]
    isiffound = binarySearch(item, list)
    if isiffound:
        print(item, "number found in the list")
    else:
        print(item, "not found in the list")
