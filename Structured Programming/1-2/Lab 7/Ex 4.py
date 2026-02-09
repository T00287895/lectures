from tkinter import simpledialog, messagebox


def isEven():
    match num % 2:
        case 0:
            return "even"
        case _:
            return "odd"
num = simpledialog.askinteger("Input", "Please enter an integer (hit return to exit)")
messagebox.showinfo("Farewel!", f"You entered {isEven()} number")
