def linearSearch(MyItem, MyList):
    found = False
    position = 0
    while position < len(MyList) and not found:
        if MyList[position] == MyItem:
            found = True
        position = position + 1
    return found


if __name__ == "__main__":
    item = int(input("Enter any number: "))
    list = [14, 21, 2, 5, 7, 12,  28, 31, 36]
    isit = linearSearch(item, list)
    if isit:
        print(item, "found in the list")
    else:
        print(item, "not found in the list")