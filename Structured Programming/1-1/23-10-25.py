# Kilobyte Day
import sys
from datetime import date

KILOBYTE_DAY = 23
KILOBYTE_MONTH = 10

discount = 0
resultPrice = 0

today = date.today()
dayNum = today.day
monthNum = today.month
monthStr = today.strftime("%b")

print(f"Tody is {dayNum} of {monthStr}.")

if dayNum != KILOBYTE_DAY or monthNum != KILOBYTE_MONTH:
    print(f"Kilobyte Day will be at {dayNum} of {monthStr}. Bye!")
    sys.exit()

try:
    price = float(input("Price: "))
except ValueError:
    price = 0
    print(f"Price must be a number!")
    pass

# int = 2.5/
# except valueError
# int = 2
# int = n/a

if price < 120 and price > 0.0:
    discount = (price / 100) * 8
elif price > 120 and price > 0.0:
    discount = (price / 100) * 16

resultPrice = price - discount

print(f"Price is {price} and discount is {discount}. Result price is {resultPrice}.")
