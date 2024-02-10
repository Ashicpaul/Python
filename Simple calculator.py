def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def higher_order(func):
    def wrapper(x, y):
        return func(x, y)
    return wrapper

def menu():
    print("Welcome to the calculator!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1/2/3/4): ")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        result = higher_order(add)(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = higher_order(subtract)(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = higher_order(multiply)(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")

menu()
