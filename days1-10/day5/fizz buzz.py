# numbersList = []
#
# for numbers in range(1,101):
#     numbersList.append(numbers)
#
# secondList = numbersList.copy()
#
# for i in range(0,(len(numbersList))):
#
#     if numbersList[i] % 3 == 0 and numbersList[i] % 5 == 0:
#         secondList[i] = "FizzBuzz"
#
#     elif numbersList[i] % 3 == 0:
#         secondList[i] = "Fizz"
#
#     elif numbersList[i] % 5 == 0:
#         secondList[i] = "Buzz"
#
# for OneLineElement in secondList:
#     print(OneLineElement)
#

# coach solution:

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)