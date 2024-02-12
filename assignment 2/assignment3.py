def sum_of_digits(num):
   
    num_str = str(num)
   
    digit_sum = sum(int(digit) for digit in num_str)
    return digit_sum

def sum_of_digits_in_list(lst):
    sums_list = [sum_of_digits(num) for num in lst]
    return sums_list


sample_input = [45, 73, 105, 7, 54, 80]
sums_output = sum_of_digits_in_list(sample_input)

print("output:", sums_output)
