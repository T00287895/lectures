from tkinter import simpledialog, messagebox

def numberOfDaysIn():
    
    if month % 2 == 0:
        days = 30
    if month == 2:
        days = 28
    elif month % 2 != 0:
        days = 31
    return days

while True:
    month = simpledialog.askinteger("Input", "Please enter the number of a month:")

    if month > 12 or month < 1:
        messagebox.showinfo("Days in Month", "Invalid - you must enter a month number between 1 and 12")
    else:
        messagebox.showinfo("Days in Month", f"There are {numberOfDaysIn()} in this month")
        break
