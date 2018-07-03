def ParisOfElements(arr, n, sum):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count = count + 1
                print("(", arr[i], ",", arr[j], ")")
    return count


arr = [1, 5, 3, 1, 7, 2, -1]
n = len(arr)
sum = 8
print("count of paris is ", ParisOfElements(arr, n, sum))
