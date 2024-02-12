def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers


sample_input = [45, 78, 4, 34, 67, 3, 93, 101, 77]
odd_numbers = print_odd_numbers(sample_input)

print("odd numbers", odd_numbers)
