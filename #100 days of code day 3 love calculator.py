#100 days of code day 3 love calcoulator

print("The Love calculator is checking your compability..")
your_name = input("Enter your name : ")
love_name = input("Enter your love's name : ")

# checking for lovers compability if their names occur much in true love
# change names to lower case and add them up
lowercase_names = your_name.lower()+love_name.lower()

# count how many times true and love occurs in the name
t = lowercase_names.count("t")
r = lowercase_names.count("r")
u = lowercase_names.count("u")
e = lowercase_names.count("e")
true = t+r+u+e

l = lowercase_names.count("l")
o = lowercase_names.count("o")
v = lowercase_names.count("v")
e = lowercase_names.count("e")
love = l+o+v+e


true = str(true)
love = str(love)
score=int(love+true)
if (score < 10) or (score > 90):
      print(f"Your Love score is {true + love}%, you can go together like coke and mentos ")
elif (score >= 40) and (score <= 50):
      print(f"Your Love score is {true + love}%, you are alright together")
else:
    print(f"Your Love score is {true + love}%, Wahala dey sha ")
