print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

payment = ((float(bill) * (1 + (int(tip)/100))) / int(split))
rouded_payment = "{:.2f}" .format(payment)
print (f"Each person should pay: ${rouded_payment} dollars ")
