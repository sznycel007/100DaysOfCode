
def my_function():
    return 3 * 2


output = my_function()
print(output)


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

# formatted_string = format_name("KARol", "kAROl")
# print(formatted_string)
print(format_name(input("What's your first name? "),input("What is your last name? ")))