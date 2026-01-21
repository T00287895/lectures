#Exercise2.py

#This program uses variables of different types for storing the details of an
#investment and then displays them nicely in a tabular form using the format
#operator % and relevant format specifiers
 

investmentType1 = input("Please enter the type of the first investment: ")

sharesPurchased1 = input("Please enter the number of shares purchased: ")

sharePrice1 = input("Please enter the share price: ")

investmentType2 = input("\n\nPlease enter the type of the second investment: ")

sharesPurchased2 = input("Please enter the number of shares purchased: ")

sharePrice2 = input("Please enter the share price: ")


print("\n\n\t\t===============================" +
       "\n\t\t\tInvestment Details" +
       "\n\t\t===============================\n\n" +
       "%-20s%-10s%-10s\n%-20s%-10s%-10s" % 
       ("Investment Type","# Shares","Share Price",
       "---------------","--------","-----------") +
       "\n%-20s%-10d%-10.4f\n%-20s%-10d%-10.4f" %
       (investmentType1,int(sharesPurchased1),float(sharePrice1),
       investmentType2,int(sharesPurchased2),float(sharePrice2)))
                                



