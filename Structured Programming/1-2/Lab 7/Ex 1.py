import math

def periodCalculator():
    p = math.pi
    g = 9.8
    t = 2 * p * math.sqrt(l/g)
    return t

l = float(input("Please enter the lenght of the pendulm: "))

print(f"The period of the pendulm is {periodCalculator():.3f} second")
