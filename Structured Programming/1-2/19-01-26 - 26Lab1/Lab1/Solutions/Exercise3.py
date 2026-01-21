#Exercise3.py

#This program reads in a number of inches and converts it to feet and inches

 
totalInches = input("Please enter the total number of inches: ")

totalInches = int(totalInches) #casting to an integer

print("\n" + str(totalInches) + "\"" + " is equivalent to " +
      str(totalInches//12) + "'" + str(totalInches - 12*(totalInches//12)) + "\"")

#Alternatively could have simply used the expression
#totalInches % 12 to get the remaining inches here
				               	
                         
