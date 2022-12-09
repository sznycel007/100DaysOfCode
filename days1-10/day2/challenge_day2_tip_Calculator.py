print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $" ))
split = int(input("How many people to split the bill ? " ))
tip = float(input("What percentage would you like to give? 10,12,15 "))


tipCalculate = tip * 0.01
AfterTipCalculate = float(tipCalculate*bill+bill)
result = AfterTipCalculate/split

print("Each person should pay: $%s" % (round(result,2)))

