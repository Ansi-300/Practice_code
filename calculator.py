def calculator():
    print("Welcome to the Calculator!")
    print("Enter an operator (+, -, *, /) and two numbers to perform calculations.")
    print("Enter 'Q' to quit the program.")

    while True:
        # Ask for the operator
        operator = input("\nEnter an operator (+, -, *, /) or 'Q' to quit: ").strip().upper()
        
        # Check if the user wants to quit
        if operator == 'Q':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        # Validate the operator
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Please enter +, -, *, or /.")
            continue
        
        # Ask for the first number
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Ask for the second number
        while True:
            try:
                num2 = float(input("Enter the second number: "))
                if operator == '/' and num2 == 0:
                    print("Division by zero is not allowed. Please enter a non-zero second number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Perform the calculation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        
        # Display the result
        print(f"The result of {num1} {operator} {num2} is: {result}")

# Run the calculator
calculator()