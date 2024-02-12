def remove_vowels(input_str):
    vowels = "aeiouAEIOU"
   
    result = ""

    for char in input_str:
   
        if char not in vowels:
            
            result += char

    return result

input_string = "Happy Coding"
output_string = remove_vowels(input_string)

print("output:", output_string)
