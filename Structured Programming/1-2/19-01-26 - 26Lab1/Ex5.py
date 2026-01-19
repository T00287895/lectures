status = 0
while True:
    height = float(input("Please enter your height: "))
    if height < 1:
        print("Invalid height! Try again")
    else:
        break
    
while True:
    weight = float(input("Please enter your weight: "))
    if weight < 15:
        print("Invalid weight! Try again")
        
    else:
        break

bmi = weight/height

if bmi < 18.5:
    status = "underweight"
elif 18.5 < bmi < 24.99:
    status = "normal"
elif 25.0 < bmi < 29.99:
    status = "overweight"
elif bmi >= 30:
    status = "obese"







print(f"Your BMI is {bmi:.2f} so you are {status}")

