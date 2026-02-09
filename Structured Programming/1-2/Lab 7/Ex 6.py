from tkinter import simpledialog, messagebox

width = simpledialog.askinteger("Input", "Please enter the width of your square graphic")
ch = simpledialog.askstring("Input", "Please enter the character that will be used in square")


square = ""
for i in range(width):
    square += f" {ch} " * width +  "\n"

messagebox.showinfo("Square graphic", square)





