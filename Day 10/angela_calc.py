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

num1 = int(input("What is the first number?: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the next number?: "))

calculation = operations[operation_symbol]
answer = calculation(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")