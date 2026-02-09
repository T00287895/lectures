#Exercise5.py

#This program reads in the weight in kg and the height in metres of a person and then
#uses a formula to determine their BMI. It then uses a table to display an appropriate
#message based on their BMI


weight = input("Please enter your weight: ")
weight = float(weight)

if(weight<0):
    print("\nInvalid weight! Quitting program now...")
else:      
    height = input("Please enter your height: ")
    height = float(height)
                
    if(height<0):
        print("\nInvalid height! Quitting program now...")
    else:
        BMI = weight/(height*height)
                                
        if(BMI<18.5):
            message = "underweight"
        elif(BMI<25):
            message = "normal"
        elif(BMI<30):
            message = "overweight"
        else:
            message = "obese"
                                
        print("\nYour BMI is " + str(BMI) + " so you are " + message)

