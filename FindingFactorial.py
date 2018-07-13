def GetFatorial(n):
    count = 1
    for i in range(1, n + 1):
        count = count * i
    return count


if __name__ == "__main__":
    n = int(input("Enter any no to find factorial: "))
    print(GetFatorial(n))
