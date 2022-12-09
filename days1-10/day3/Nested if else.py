print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child ticket are $5 ")
    elif age <= 18:
        bill = 7
        print("Adult ticket are $7")
    elif age in range(45,55):
        print("Age 45-55 - go for free $0")
    else:
        bill = 12
        print("Adult ticket are $12")

    wants_photo = input("Do you want extra photo from ride? Y or N ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("You are not allowed to use this type of rollercoaster")