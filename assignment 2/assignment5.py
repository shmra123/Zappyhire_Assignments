def max_frequency_char(string):
    
    string = string.lower()
    
    
    char_freq = {}
    
    
    for char in string:
        if char.isalpha():  
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    
    max_freq_char = max(char_freq, key=char_freq.get)
    
    return max_freq_char


sample_input = "Grass is greener on the other side"
max_freq_character = max_frequency_char(sample_input)

print(f"Most repeating letter is \"{max_freq_character}\"")
