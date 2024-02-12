def is_palindrome(word):
     
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


user_input = input("Enter a word: ")


if is_palindrome(user_input):
    print(f"Yes! \"{user_input}\" is a palindrome.")
else:
    print(f"No, \"{user_input}\" is not a palindrome.")
