
firstInvestment = input("Please enter the type of the first investmen: ")
firstNumberOfPurchased = int(input("Please enter the number of shares purchased: "))
firstPrice = float(input("Please enter the price per share: "))

print("\n")

secondInvestment = input("Please enter the type of the first investmen: ")
secondNumberOfPurchased = int(input("Please enter the number of shares purchased: "))
secondPrice = float(input("Please enter the price per share: "))

print("\n", "=" * 10, sep="")
print("Investment Details")
print("=" * 10)

print("\n")

print("%-30s%-30s%-30s" % ("Investment Type", "# Shares", "Share Price"))
print("%-30s%-30s%-30s" % ("--------", "--------", "--------"))
print("%-30s%-30s%-30s" % ("Mutual Fund", firstNumberOfPurchased , f"{firstPrice:.2f}"))
print("%-30s%-30s%-30s" % ("Consensus Fund", secondNumberOfPurchased, f"{secondPrice:.2f}"))