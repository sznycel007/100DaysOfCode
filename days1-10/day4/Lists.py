# https://docs.python.org/3.10/tutorial/datastructures.html#more-on-lists
states_of_america = ["Delware","Pennsylvawnia","New Jersey","Georgia","New York","Utah","Alaska","Hawaii","Ohio","Texas","Iowa","Montana","Kansas"]

print(states_of_america)

print(states_of_america[2])
print(states_of_america[-1])
print(states_of_america[-3])

states_of_america.append("KaroLand")
print(states_of_america)


states_of_america.extend(["KarolanaLand","Jack Bauer Land"])
print(states_of_america)
print('-'*30)

# list in the list:

dirty_dozen = ["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]

fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

#nested list
dirty_dozen = [fruits,vegetables]

print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
