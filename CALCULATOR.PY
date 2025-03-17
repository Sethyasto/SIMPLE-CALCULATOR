def calculate(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Division by zero is undefined.")
    else:
        print("Invalid operation. Please choose addition (+), subtraction (-), multiplication (*), or division (/).")


# Get user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Call the function with user inputs
calculate(num1, num2, operation)