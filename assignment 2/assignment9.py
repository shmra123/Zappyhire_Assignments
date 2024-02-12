def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        while n > 0:
            result *= n
            n -= 1
        return result

num = int(input("Enter a number: "))

fact = factorial(num)


print("Factorial of", num, "is", fact)
