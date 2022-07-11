def add(f_number, s_number):
    return f_number + s_number


def subtract(f_number, s_number):
    return f_number - s_number


def multiply(f_number, s_number):
    return f_number * s_number


def divide(f_number, s_number):
    return f_number / s_number


operations = {
    "+": add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    end = False
    f_number = float(input("Whats the first number?: "))
    for keys in operations:
        print(keys)
    while not end:
        operator = input("Pick an operation: ")
        s_number = float(input("What's the second number?: "))
        result = operations[operator](f_number, s_number)
        print(f"{f_number} {operator} {s_number} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: \n") == 'n':
            end = True
            calculator()
        else:
            f_number = result


calculator()
