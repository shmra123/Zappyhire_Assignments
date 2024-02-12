sample_input = [34, "word", 4.5, "code", 89, 9.0]

result_dict = {}


for item in sample_input:
    
    data_type = type(item).__name__
   
    if data_type in result_dict: 
        result_dict[data_type].append(item)
    else:

        result_dict[data_type] = [item]

print(result_dict)
