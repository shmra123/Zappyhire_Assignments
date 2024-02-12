def find_largest(arr):
    if len(arr) == 0:
        return None

    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num

    return largest

# Sample input
input_arr = [45, 56, 98, 3, 67, 9, 90]
largest_num = find_largest(input_arr)

if largest_num is not None:
    print("Largest number is", largest_num)
else:
    print("Array is empty.")
