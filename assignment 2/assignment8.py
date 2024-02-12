def reverse_items_tuple(input_tuple):
   
    reversed_list = list(input_tuple)

    for i in range(len(reversed_list)):
 
        if isinstance(reversed_list[i], str):
     
            reversed_list[i] = reversed_list[i][::-1]


    reversed_tuple = tuple(reversed_list)
    return reversed_tuple


input_tuple = ("abc", 567, "python", "try", 87)
output_tuple = reverse_items_tuple(input_tuple)

print("output", output_tuple)
