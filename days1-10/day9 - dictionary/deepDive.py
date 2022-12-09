programming_Dictionary = {
    "Bug": "An error in a program that prevents program from running as expected.",
    123: "A piece of code that you can easily call over and over again",

}

# Retrieving items from dictionary
print(programming_Dictionary[123])
print(programming_Dictionary["Bug"])

# Adding new items to dictionary

programming_Dictionary["Loop"] = "The action of doing something over and over again"
print(programming_Dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
#programming_Dictionary = {}
print(programming_Dictionary)

# Edit an item in a dictionary
programming_Dictionary["Bug"] = "A moth in your computer"
print(programming_Dictionary)

print()
# Loop through a dictionary

for key in programming_Dictionary:
    print(key)
    print(programming_Dictionary[key])

