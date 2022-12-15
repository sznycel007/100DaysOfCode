import calc_logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(calc_logo.logo)

    num1 = float(input("What's the first number? "))
    for key in operations:
        print(key)
    should_continue = True
    # function = operations["+"]
    # print(function(3, 2))
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number? "))
        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()










