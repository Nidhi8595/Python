def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def pdt(x, y):
    return x * y

def quotient(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def remainder(x, y):
    return x % y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter your choice -> ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number -> "))
        num2 = float(input("Enter second number -> "))

        if choice == '1':
            print(f"The sum is :- {sum(num1, num2)}")

        elif choice == '2':
            print(f"The Difference is :- {diff(num1, num2)}")

        elif choice == '3':
            print(f"The Product is :- {pdt(num1, num2)}")

        elif choice == '4':
            print(f"The result is :- {quotient(num1, num2)}")

        elif choice == '4':
            print(f"The result is :- {remainder(num1, num2)}")
    else:
        print("Invalid input")

calculator()