import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")
nr_letter = int(input("How many letter would you like in your password?\n"))
nr_number = int(input("How many numbers would you like ?\n"))
nr_symbols = int(input("How many symbols would you like ?\n"))

password = []
for letter in range(0,nr_letter):
    password.append(random.choice(letters))

for letter in range(0,nr_number):
    password.append(random.choice(numbers))

for letter in range(0, nr_symbols):
    password.append(random.choice(symbols))

print(''.join(password))
random.shuffle(password)

print("shuffled password below:")
print(''.join(password))


# teacher approach - easy one

# password = ""
# for char in range(1,nr_letter+1):
#     randomChar = random.choice(letters)
#     password += randomChar
#
# for char in range(1,nr_number+1):
#     randomChar = random.choice(numbers)
#     password += randomChar
#
# for char in range(1,nr_symbols+1):
#     randomChar = random.choice(symbols)
#     password += randomChar
#
# print(password)


