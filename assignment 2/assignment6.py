def contains_substring(main_string, substring):
    
    if substring in main_string:
        return True
    else:
        return False


main_string = "Grass is greener on the other side"
substring_input = "other"
result = contains_substring(main_string, substring_input)

print(result)
