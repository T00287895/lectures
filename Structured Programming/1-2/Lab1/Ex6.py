while True:
    word = input("Please enter a word: ")
    if len(word) < 9:
        print("Word is too short! Try again")
    elif len(word) > 9:
        print("Word is too long! Try again")
    elif any(char.isdigit() for char in word):
        print("Word cannot contain digits! Try again")
    elif word[0] != word[-1] and word[1] != word[-2] and word[2] != word[-3] and word[3] != word[-4]:
        print("The word is not palindrome! Try again")
    else:
        break
print("The word you have entered is palindrome!")