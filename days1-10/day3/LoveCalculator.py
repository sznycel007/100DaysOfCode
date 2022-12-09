# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

firstWord = "TRUE"
secondWord = "LOVE"

UpperName1 = name1.upper()
UppperCase2 = name2.upper()

emptyList1 = []
emptyList2 = []
# counting TRUE

for letter in firstWord:
     firstCounter = int(UpperName1.count(letter))
     emptyList1.append(firstCounter)

     secondCouter = int(UppperCase2.count(letter))
     emptyList2.append(secondCouter)

sum1 = (sum(emptyList1))
sum2 = (sum(emptyList2))
summaryOfTrue = sum1+sum2

emptyList1 = []
emptyList2 = []

# counting Love
for letter in secondWord:
     firstCounter = int(UpperName1.count(letter))
     emptyList1.append(firstCounter)

     secondCouter = int(UppperCase2.count(letter))
     emptyList2.append(secondCouter)

sum1 = (sum(emptyList1))
sum2 = (sum(emptyList2))

summaryOfLove = sum1+sum2

wordsSummary = (str(summaryOfTrue)+str(summaryOfLove))
IntwordsSummary = int(wordsSummary)

if IntwordsSummary < 10 or IntwordsSummary > 90:
    print(f"Your score is {IntwordsSummary}, you go together like coke and mentos.")

elif IntwordsSummary in range(40,50):
    print(f"Your score is {IntwordsSummary}, you are alright together.")

else:
    print(f"Your score is {IntwordsSummary}.")