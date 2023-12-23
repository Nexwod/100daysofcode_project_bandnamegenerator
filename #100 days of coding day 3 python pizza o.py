#100 days of coding day 3 python pizza order program
 # create a greeting for your program
print("Thank you for choosing Nexwod Python Pizza Deliveries!")

# aske the user for their order
size = input("What size of Pizza do you wish to have? Enter 'L' for large, 'M' for Medium and 'S' for small\n" )
add_pepperoni = input("Do you want Pepperoni? Enter 'Y' for Yes, 'N' for No\n")
extra_cheese = input("Do you want Extra Cheese? Enter 'Y' for Yes, 'N' for No\n")

# set the pizza prices 
price = 0

# program the order
if add_pepperoni == 'Y':
    price += 3 
if extra_cheese == 'Y':
    price += 1 
if size == 'S':
    price += 15
elif size == 'M':
    price += 20
elif size == 'L':
    price += 25


print(f"Your final bill is: {price}")