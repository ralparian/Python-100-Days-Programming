print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? (10, 12, 15?)"))
split = int(input("How many people to split the bill?"))

total_tip = bill * (tip / 100)
payperson = (total_tip / split) + (bill / split)
round_split = "{:.2f}".format(payperson)
print(f"Each person should pay: {round_split}")
