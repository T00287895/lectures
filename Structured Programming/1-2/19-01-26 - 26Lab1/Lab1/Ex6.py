while True:
    word = input("Please enter a word: ")
    if len(word) < 9:
        print("Word is too short! Try again")
    elif len(word) > 9:
        print("Word is too long! Try again")
    elif any(char.isdigit() for char in word):
        print("Word cannot contain digits! Try again")
    elif word[0:8] != word[]:
        print("The word is not palindrome! Try again")
    else:
        break
print("The word you have entered is palindrome")