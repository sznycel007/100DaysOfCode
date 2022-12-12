import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
chosen_word_list = []
for x in chosen_word:
    chosen_word_list.append(x)
# print(chosen_word_list)

for _ in range(len(chosen_word)):
    display += "_"

while "_" in display and display != chosen_word_list:

    i = 0
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display[i] = letter
        else:
            pass
        i +=1

    joined = (''.join(display))
    print(joined)
print("User win!")







