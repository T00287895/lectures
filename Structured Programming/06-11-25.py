# Federal Tax Rate

def getInputNum(promptText):
    print(promptText)
    value = 0
    while value == 0:
        try:
            _value = float(input("Enter a number: "))
            value = _value
        except ValueError:
            print("Please enter a number.")
    return value


def getMarriedStatusStr():
    _value = input("Enter your married status: ")
    if (_value == "single" or _value == "maried"):
        return _value
    print("Your married status is either 'single' or 'maried'.")
    return getMarriedStatusStr()


incomeNum = getInputNum("What is your income?")

print("Are you married?")
marriedStatusStr = getMarriedStatusStr()

resultData = {
    "taxesSum": 0,
    "taxesProc": "",
    "income": incomeNum,
}

if (marriedStatusStr == "maried"):
    if (incomeNum < 64000):
        resultData["taxesSum"] = (incomeNum / 100) * 10
        resultData["taxesProc"] = f"{10}%"
    elif (incomeNum > 64000):
        resultData["taxesSum"] = ((incomeNum / 100) * 25) + 6400
        resultData["taxesProc"] = f"{25}% + 6400USD"
elif (marriedStatusStr == "single"):
    if (incomeNum < 32000):
        resultData["taxesSum"] = (incomeNum / 100) * 10
        resultData["taxesProc"] = f"{10}%"
    elif (incomeNum > 32000):
        resultData["taxesSum"] = ((incomeNum / 100) * 25) + 3200
        resultData["taxesProc"] = f"{25}%"

print(
    f"Your income is less than {resultData['income']}. "
    f"Taxes: {resultData['taxesProc']}. "
    f"Result: {resultData['taxesSum']} USD."
)
