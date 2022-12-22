# modifying global scope

enemies = 1


def increase_enemies():
    # modifying global scope by local scope is not welcome in Python - use return option to operate with global value
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# using return

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    return enemies

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# having global scopes could be useful for instance with Global Constant like pi, etc...

# Global Constants

# uppercase + separate by underscore

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@kw_karol"
