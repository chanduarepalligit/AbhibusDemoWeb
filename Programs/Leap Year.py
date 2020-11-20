year = 1604
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not an leap year")
    else:
        print("Leap year")
else:
    print("Not an leap year")

year1 = 2004
if year1 % 4 == 0 and year1 % 100 != 0 or year1 % 400 == 0:
    print("Leap year")
else:
    print("Not an leap year")
