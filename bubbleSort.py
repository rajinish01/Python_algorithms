def bubbleSort(mylist):
    moreSwaps = True
    while moreSwaps:
        moreSwaps = False
        for element in range(len(mylist) - 1):
            if mylist[element] > mylist[element + 1]:
                moreSwaps = True
                temp = mylist[element]
                mylist[element] = mylist[element + 1]
                mylist[element + 1] = temp
    return mylist

#def bblsort():
if __name__ == "__main__":
    mylist = [5, 2, 7, 1, 9, 3, 6]
    sortdlist = bubbleSort(mylist)
    print(sortdlist)
