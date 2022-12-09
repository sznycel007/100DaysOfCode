# 🚨 Don't change the code below 👇
row1 = ["A️","B️ "," C️"]
row2 = ["D️","E️ "," F️"]
row3 = ["G️","H️ "," I️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

map[vertical-1][horizontal-1] = "X"


#Write your code above this row 👆
print('-'*30)
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

