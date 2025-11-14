import random

print("Welcome to the Cho-Han Game!")
print("Guess whether the total of two dice will be even (Cho) or odd (Han).")

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

guess = input("Enter your guess (Cho or Han): ").strip().lower()

if total % 2 == 0:
    result = "cho"

else:
    result = "han"

print(f"The dice show: {die1} and {die2} (Total = {total})")

if guess == result:
    print("Congratulations! You guessed correctly 🎉")
else:
    print("Sorry, you lost 😅")

print("Thanks for playing!")
