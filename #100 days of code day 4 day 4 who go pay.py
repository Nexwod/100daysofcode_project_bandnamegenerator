#100 days of code day 4 day 4 who go pay
import random
names = ['Angela', 'Ada', 'Jenny']
length= len(names) - 1
id_of_payer = random.randint(0,length)
payer = names[id_of_payer]
print(f"{payer} is going to buy the meal today")
