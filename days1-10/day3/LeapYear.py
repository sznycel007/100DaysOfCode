year = int(input("Which year you want to check? "))

def leapOrnot(year):

    # if (year % 4 == 0 and year % 400 == 0) or year % 100 == 0:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                print("Leap year.")
            else:
                print("Not Leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

leapOrnot(year)
