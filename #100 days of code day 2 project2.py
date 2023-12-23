#100 days of code day 2 project2
# create a greeting for your program
print("Welcome to Tip Calculator!")

# asked the user for the total bill
bill = float(input("What's the total bill? \n" ))

# ask the user for the percentage
percentage = float(input("What's percentage tip would you like to give? 10, 12 or 15? \n" ))

#number of people to  split the bill
people = float(input("How many people are to split the bill? \n" ))

# calculate for it 
calpercentage = percentage/100 + 1
totalbill = bill * calpercentage
eachamount = round(totalbill/people, 2)

print(f"Each Person should pay {eachamount}")