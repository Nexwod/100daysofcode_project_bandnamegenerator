#100 days of code day 3 project treasure island
# create a greeting for your program
print("Welcome to Treasure Island")
print("Your mission is to find the treasure and send it to me")

first = input("You are on a cross road? type 'L' for left or 'R' for right\n")
first = first.lower()
if first == "l":
    second = input("You come to a lake. There is an Island is the middle of the lake. Type 'W' to wait for a boat or 'S' to swim across\n")
    second = second.lower()
    if second == "w":
        third = input("You arrive at the Island unharmed. There is a house with 3 doors.one Red, One Yellow and one blue. Which color do you choose?  Type 'R', 'Y' or 'B'\n")
        third = third.lower()
        if third == "y":
           print("You win, Now send this to Nexwod to claim your reward\n")
        else:
            print("You entered the carnibals home, Game Over!!")
    else:
        print("You died while swimming, Game Over!!")
else:
    print("Game Over!!")


