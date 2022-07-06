#1. Show a welcome message for the user
print("Hello there, welcome to the tip calculator!")

#2. Get the total bill, the percentage of the tip and how many people will split the total
bill = float(input("What was the total bill?\n$"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
split = float(input("How many people to split the bill?\n"))

#3. Now do the math
total_bill = bill + (bill * (tip_percentage / 100))
each_part = total_bill / split
round_each_part = "{:.2f}".format(each_part)

#4. Show the result, as a flot, with the cents in two decimals
print(f"Each person should pay: ${round_each_part}")