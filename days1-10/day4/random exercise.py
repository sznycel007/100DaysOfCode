import random
import my_module

print(my_module.pi)

random_integer = random.randint(1,10)

print("random int:",random_integer)
# default scope for random.random is 0.00 - 0.99
# this is how to generate float number from 0.00 - 0.99 * 5
print("random float:",random.random()*5)


love_score = random.randint(1,100)
print(f"Your love score is {love_score}")