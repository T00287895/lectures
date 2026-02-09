investment = input("Please enter the type of the first investment: ") or "Mutual Fund"
shares = int(input("Please enter the number of shares purchased: ")) 
share_price = float(input("Please enter the share price"))
investment_2 = input("\nPlease enter the type of the second investment: ") or "Consensus Fund"
shares_2 = int(input("Please enter the number of shares purchased: ")) 
share_price_2 = float(input("Please enter the share price"))
print("\n\n        ======================== \n          Investment Details \n        -------------------------\n")

print("%-25s" % "Invesment Type", "%-10s" % "# Shares", "%-15s" % "Share Price")
print("%-25s" % "--------------", "%-10s" % "--------", "%-15s" % "-----------")
print("%-25s" % (investment), "%-10d" % (shares), "%-15.4f" % (share_price))
print("%-25s" % (investment_2), "%-10d" % (shares_2), "%-15.4f" % (share_price_2))
