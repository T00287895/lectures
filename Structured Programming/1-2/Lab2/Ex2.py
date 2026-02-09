while True:

    t_number = input("Please enter the students T-number: ").lower()
    if t_number[0] != 't':
        print("Invalid! The t-number must start with a 't'. Try again.")
    elif len(t_number) != 9:
        print("Invalid! The t-number must be 9 characters long. Try again.")
    elif not t_number[1:].isdigit():
        print("Invalid! The last 8 characters must be digits. Try again.")

    else:
        print("It is a valid t-number.Thank you!")
        break