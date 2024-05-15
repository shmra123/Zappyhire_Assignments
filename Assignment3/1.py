def MyFunction(l1):
    l1.sort()
    small = l1[0]
    large = l1[-1]
    print("Largest number is", large, "Smallest number is", small)

a = [45, 56, 98, 3, 67, 9, 90]
MyFunction(a)
