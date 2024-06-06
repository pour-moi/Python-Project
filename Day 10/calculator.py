from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
continue_caluculating = True
first_number = float(input("What is the first number: "))
while continue_caluculating:
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick operation you want to perform: ")
    calculation_operation = operations[operation_symbol]
    second_number = float(input("What is the next number: "))

    final_result = calculation_operation(first_number, second_number)

    print(f"{first_number} {operation_symbol} {second_number} = {final_result}")

    choice = input(f"Type 'y' to continue calculatin with {final_result},type 'n' to start a new calculation or type e to exit ")
    if choice == 'y':
        first_number = final_result
    elif choice == 'n':
        first_number = float(input("What is the first number: "))
    elif choice == 'e':
        continue_caluculating = False


