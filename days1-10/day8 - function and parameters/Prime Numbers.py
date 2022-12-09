# Liczba pierwsza - to taka liczba naturalna, która ma dokładnie dwa dzielniki naturalne (nie wiecej)
#Write your code below this line 👇



# def prime_checker(number):
#     if number % 1 == 0 and number % number == 0 and :
#         print(f"{number} is prime!")
#
#
# #Write your code above this line 👆
#
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

def is_prime(number):
    is_prime = True
    for i in range(2,number):
        if (number%i) == 0:
            is_prime = False
    if is_prime:
        print("It'a a prime number")
    else:
        print("It's not a prime number")

n = int(input("Check this number: "))
is_prime(n)