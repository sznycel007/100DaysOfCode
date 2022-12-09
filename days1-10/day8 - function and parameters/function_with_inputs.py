#               something =  123
#               parameter  | argument
def my_function(something):
    #Do this
    #Then do this
    #Finally do this

    def greet(name):
        print(f"Hello {name}!")

    greet('Karol')


# function with more than 1 input

def greet_with(name,location):
    print(f"Hello {name} welcome in {location}")

greet_with('Karol','Harlem')

greet_with(location='Harlem',name='Karol')