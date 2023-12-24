#100 days of code day 4 Pirate Map
import random

line1 = ["0", "0", "0",]
line2 = ["0", "0", "0",]
line3 = ["0", "0", "0",]
print("Marking your Treasure X marks the spot")
position = input()
position = position.lower()
map = [line1, line2, line3]
a = position.count("a")
b = position.count("b")
c = position.count("c")

num1 = position.count("1")
num2 = position.count("2")
num3 = position.count("3")
if  a == 1:
    line=line1
elif  b == 1:
    line=line2
elif  c == 1:
    line=line3
else:
    print("Not found")

if  num1 == 1:
    i=0
elif  num2 == 1:
    i=1
elif  num3 == 1:
    i=2
else:
    print("Not found")
line[i]='X'
print(f"{line1}\n{line2}\n{line3}")
