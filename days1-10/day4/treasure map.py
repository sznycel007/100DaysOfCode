# ð¨ Don't change the code below ð
row1 = ["Aï¸","Bï¸ "," Cï¸"]
row2 = ["Dï¸","Eï¸ "," Fï¸"]
row3 = ["Gï¸","Hï¸ "," Iï¸"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ð¨ Don't change the code above ð

#Write your code below this row ð

horizontal = int(position[0])
vertical = int(position[1])

map[vertical-1][horizontal-1] = "X"


#Write your code above this row ð
print('-'*30)
# ð¨ Don't change the code below ð
print(f"{row1}\n{row2}\n{row3}")

