swap = lambda x, y: (y, x)

var_one = input("Enter the first variable: ")
var_two = input("Enter the second variable: ")
print("Before swapping: First variable =", var_one, "Second variable:", var_two)
var_one, var_two = swap(var_one, var_two)
print("After swapping: First variable =", var_one, "Second variable:", var_two)
