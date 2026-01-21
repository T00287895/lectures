num_amount = 0
sum_numbers = 0
odd_numbers = 0
greater_100 = 0
word = "first"
word_num = 0

while True:
    if word_num >= 1:
        word = "next"
    number = int(input(f"Please enter a {word} positive integer: "))
    if number == -1:
        print("You have exited the program.")
        break
    elif number < -1:
        print("Invalid input, please enter a postive integer or -1 to exit.")
    else:
        if number > 100:
            greater_100 += 1
        elif number % 2 != 0:
            odd_numbers += 1
        elif number % 2 != 0 and number > 100:
            odd_numbers += 1
            greater_100 += 1
        sum_numbers += number
        num_amount += 1
        word_num += 1


print(f"\n", "=" * 7, "Results", "=" * 7 )
print(f"\nNumber of values entered: {num_amount}")
print(f"Number of odd values entered: {odd_numbers}")
print(f"Number of values > 100  entered: {greater_100}")
print(f"Avarage of the values you have entered: {sum_numbers / num_amount:.0f}")