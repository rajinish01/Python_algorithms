def Getfactorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
        continue
    return factorial


if __name__ == "__main__":
    print(Getfactorial(10))