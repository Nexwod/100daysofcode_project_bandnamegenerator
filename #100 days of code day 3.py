#100 days of code day 3
year = int(input())

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap Year")
    else:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
else:
    print("Not Leap year")  