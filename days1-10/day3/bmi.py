# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def bmi(height,weight):
    bmi = weight/height**2
    roundedBmi = round(bmi)

    print("{} ÷ ({} x {}) = {}".format(weight, height, height, bmi))

    if roundedBmi in range(18,22):
        print("Your BMI is {}, you are underweight.".format(roundedBmi))
    elif roundedBmi in range(23,25):
        print("Your BMI is {}, you have a normal weight.".format(roundedBmi))
    elif roundedBmi in range(26,33):
        print("Your BMI is {}, you are slightly overweight.".format(roundedBmi))
    elif roundedBmi >=33:
        print("Your BMI is {}, you are obese.".format(roundedBmi))
    else:
        print("Your BMI is {}, you are clinically obese.".format(roundedBmi))


    return roundedBmi

bmi(height,weight)


