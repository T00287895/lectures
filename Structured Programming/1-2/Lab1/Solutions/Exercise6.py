#Exercise6.py

#This program reads in a word from the user and checks to ensure it contains
#exactly 9 characters. If it does it then processes the word to see whether
#it is a palindrome

 
word = input("Please enter a word 9 characters long: ")

if(len(word) != 9):
    print("\nInvalid word! Quitting program now...")
else:
    if(word[0] == word[8] and word[1] == word[7] and word[2] == word[6] and
       word[3] == word[5]):
        print("\nThe word you entered is a palindrome")
    else:
        print("\nThe word you entered is not a palindrome")
                        

